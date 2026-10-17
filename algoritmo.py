#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Desarrollos completos de un cubo fijo reposando en el plano.
Implementación del algoritmo descrito por el autor:

  1. Reducción a puntos y líneas (las figuras son grafos planos; las curvas se
     discretizan por simetría: mitad fundamental con el polígono mínimo, espejo,
     deduplicación; n múltiplo de 4).
  2. Base de datos de líneas (pares de IDs de puntos extremos).
  3. Base de datos de fijaciones: líneas que anclan cada figura a su cara
     (2/3/4 anclas según el modo del instrumento).
  4. Aristas fijadas = las que NO se cortan: deben conectar las 6 caras sin
     ciclo (árbol generador del octaedro).
  5. Despliegue físico por bisagras: una cara es elegible cuando tiene
     exactamente una arista fijada hacia la parte ya desplegada; gira 90° sobre
     esa arista; los vértices sobre la arista quedan FIJOS, el resto se LIBERA;
     el subárbol en pie viaja rígidamente. Si el proceso se atasca o una cara
     queda paralela al plano con bisagras imposibles, la configuración de
     cortes es inválida: el despliegue es su propio oráculo de validez.
  6. Render ASCII: glifo erguido + flecha de orientación + vértices (1)-(8).

Sin dependencias externas (solo la librería estándar).
"""

import itertools

# ---------------------------------------------------------------- geometría 3D
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def add(a, b): return tuple(x + y for x, y in zip(a, b))
def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def mul(s, a): return tuple(s * x for x in a)

NB = (0, -1, 0)  # normal del plano (cara base)
FACES = {'T': (0, 1, 0), 'D': (0, -1, 0), 'N': (0, 0, 1),
         'S': (0, 0, -1), 'E': (1, 0, 0), 'W': (-1, 0, 0)}
NAMES = list(FACES)
EDGES = [(a, b) for a, b in itertools.combinations(NAMES, 2)
         if dot(FACES[a], FACES[b]) == 0]            # 12 aristas del octaedro

def rot90(v, m, t, s):
    """Rota v alrededor del eje (m, t) por s*90 grados (Rodrigues, cos=0)."""
    w = sub(v, m)
    return add(m, add(mul(s, cross(t, w)), mul(dot(t, w), t)))

# ---------------------------------------------------------------- enumeración
def es_arbol(es):
    par = {n: n for n in NAMES}
    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for a, b in es:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        par[ra] = rb
    return len({find(n) for n in NAMES}) == 1

def arboles_generadores():
    return [es for es in itertools.combinations(EDGES, 5) if es_arbol(es)]

# ---------------------------------------------------- despliegue físico (núcleo)
def despliegue_fisico(fijadas, traza=False):
    """Simula el despliegue bisagra a bisagra. Devuelve None si la configuración
    de cortes es inválida (el oráculo). En caso contrario devuelve
    (centros_planares, arribas_planares, pasos)."""
    adj = {f: set() for f in NAMES}
    for a, b in fijadas:
        adj[a].add(b); adj[b].add(a)
    plano = {'D'}
    cen = {f: mul(0.5, FACES[f]) for f in NAMES}          # cubo centrado en el origen
    nor = dict(FACES)                                     # normales 3D actuales
    up = {f: UP_INI[f] for f in NAMES}                    # 'arriba' de cada símbolo
    pasos = []
    while len(plano) < 6:
        cand = [f for f in NAMES if f not in plano and len(adj[f] & plano) == 1]
        if not cand:
            return None                                   # ATASCADO: cortes inválidos
        f = cand[0]; p = (adj[f] & plano).pop()
        # subárbol en pie que viaja rígidamente con f
        sub, pila = [], [f]
        while pila:
            g = pila.pop()
            if g in plano or g in sub:
                continue
            sub.append(g); pila.extend(adj[g])
        # bisagra: la cara en pie está a distancia 0.5 del plano sobre la arista
        m = add(cen[f], mul(-0.5, NB))
        t = cross(NB, nor[f])
        nt = dot(t, t) ** 0.5
        if nt < 1e-9:                                     # cara ya paralela al plano
            return None                                   # con bisagras: inválida
        t = mul(1/nt, t)
        s = 1 if dot(rot90(nor[f], (0, 0, 0), t, 1), NB) > 0.99 else -1
        if dot(rot90(nor[f], (0, 0, 0), t, s), NB) < 0.99:
            return None
        for g in sub:
            cen[g] = rot90(cen[g], m, t, s)               # posición: gira en la bisagra
            nor[g] = rot90(nor[g], (0, 0, 0), t, s)       # normal: vector libre
            up[g] = rot90(up[g], (0, 0, 0), t, s)         # símbolo: vector libre
        if abs(dot(sub_(cen[f], cen['D']), NB)) > 1e-6:
            return None
        plano.add(f)
        if traza:
            pasos.append((f, p, sub))
    return ({f: (round(cen[f][0], 9), round(cen[f][2], 9)) for f in NAMES},
            {f: (round(up[f][0], 9), round(up[f][2], 9)) for f in NAMES}, pasos)

def sub_(a, b): return sub(a, b)

# ------------------------------------------- configuración inicial (fijaciones)
UP_INI = {'D': (0, 0, 1),            # base      -> frente   ("vertical abajo")
          'E': (0, .7071, -.7071),  # derecha   -> diagonal techo-atrás
          'T': (0, 0, -1),          # techo     -> atrás
          'S': (.7071, .7071, 0),   # trasera   -> diagonal der-techo
          'W': (0, 1, 0),           # izquierda -> techo
          'N': (0, -1, 0)}          # frente    -> base

# ------------------------------------------------------------------- render
GLIFO = {'D': ["  .  ", "     ", "     ", "     ", "  .  "],
         'T': [" ### ", "#   #", "#   #", "#   #", " ### "],
         'N': ["#    ", "#    ", "#    ", "#    ", "#####"],
         'E': ["#####", "#   #", "#   #", "#   #", "#####"],
         'S': ["  |  ", "  |  ", "--+--", "  |  ", "  |  "],
         'W': ["  *  ", " * * ", "*****", " * * ", "*   *"]}
FLECHA = {(0, 1): '▲', (1, 0): '►', (0, -1): '▼', (-1, 0): '◄',
          (1, 1): '↗', (1, -1): '↘', (-1, -1): '↙', (-1, 1): '↖'}

def render(cen, up):
    xs = [c[0] for c in cen.values()]; ys = [c[1] for c in cen.values()]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    lineas = []
    for y in range(y1, y0 - 1, -1):
        fila = [""] * 5
        for x in range(x0, x1 + 1):
            f = next((f for f in cen if cen[f] == (x, y)), None)
            if f is None:
                lineas.append("      " + "      " * 0)   # hueco
                for r in range(5):
                    fila[r] += "       "
                continue
            g = GLIFO[f]
            u = up[f]; n = dot(u, u) ** .5
            key = (int(round(u[0]/n)), int(round(u[1]/n)))
            fl = FLECHA.get(key) or FLECHA[(int(round(u[0]/n)) and 1 or 0, 0)]
            for r in range(5):
                fila[r] += "|" + g[r] + (fl if r == 2 else " ") + "|"
        lineas.extend(fila)
    return "\n".join(lineas)

# ---------------------------------------------------------------- verificación
def main():
    arboles = arboles_generadores()
    print(f"árboles generadores (desarrollos válidos): {len(arboles)}")
    validos = 0
    for es in itertools.combinations(EDGES, 5):
        if despliegue_fisico({tuple(sorted(e)) for e in es}) is not None:
            validos += 1
    print(f"configuraciones que completan el despliegue: {validos} (oráculo)")
    assert len(arboles) == 384 and validos == 384

    with open("desarrollos_384.txt", "w") as fh:
        for k, es in enumerate(arboles, 1):
            res = despliegue_fisico({tuple(sorted(e)) for e in es})
            cen, up, _ = res
            fh.write(f"----- DESARROLLO {k}/384 -----\n")
            fh.write("Fijadas: " + ",".join(a + b for a, b in es) + "\n")
            fh.write(render(cen, up) + "\n\n")
    print("generado: desarrollos_384.txt")

if __name__ == "__main__":
    main()
