# Desarrollos completos de un cubo fijo reposando en el plano
### Problema paramétrico de razonamiento espacial para la evaluación de sistemas de IA

**Autor:** Miguel Quintana Villalba — **DOI:** 10.5281/zenodo.23427484 — **Licencia:** CC-BY-4.0

## Enunciado

Mediante el uso de caracteres ASCII, desplegar en el plano todas las formas diferentes en que
es posible desarrollar un cubo **fijo** que **reposa** en ese plano (no puede levantarse) y que
tiene en sus caras seis símbolos simples: un punto, un círculo, un triángulo rectángulo, un
cuadrado, una cruz alagada y una estrella de cinco puntas. El desarrollo se realiza cortando
aristas con un bisturí de forma que ninguna cara quede desconectada del resto.

## Estructura del problema: tres capas anidadas

1. **Interpretación del enunciado**: "fijo" y "reposa" son restricciones físicas (la cara base
   está anclada al plano; el cubo no se levanta). Los sistemas de IA tienden a tratarlas como
   decoración léxica.
2. **Visualización espacial en el plano**: el desarrollo se ejecuta por bisagras, como en el
   mundo físico (ver algoritmo).
3. **Rotación coherente de las figuras**: los símbolos deben aparecer en el plano con la
   orientación que resulta del plegado, manteniendo coherencia con la configuración inicial.
   Es el constructo de los tests psicométricos de rotación mental.

## Algoritmo

1. **Reducción a puntos y líneas**: todo símbolo es un grafo plano. Se numeran todos los
   puntos y todas las intersecciones.
2. **Curvas**: toda curva se discretiza por simetría — la mitad fundamental se representa con
   el polígono de menos vértices que la aproxime, se espeja y se deduplican los puntos del
   eje. El círculo es el polígono regular de n = 12 vértices (n múltiplo de 4 y mayor que el
   máximo de vértices de las figuras poligonales presentes: la estrella, con 10).
3. **Fijaciones**: líneas que unen vértices de las caras del cubo con vértices de las figuras;
   anclan cada figura rígidamente a su cara. El número de anclas es un parámetro del
   instrumento: 2 (mínimo — comprueba si la fiabilidad del modelo es real), 3 (mide velocidad
   de deducción), 4 (redundante — comprueba capacidad deductiva pura en modelos débiles).
4. **Enumeración de cortes**: las aristas fijadas (no cortadas) deben conectar las 6 caras sin
   ciclo: un árbol generador del grafo de adyacencia de caras (octaedro). Hay C(12,5) = 792
   configuraciones candidatas.
5. **Despliegue físico por bisagras**: una cara es elegible cuando tiene exactamente una
   arista fijada hacia la parte ya desplegada. Gira 90° alrededor de esa arista hasta
   coplanaridad; los vértices sobre la arista quedan fijos, el resto se libera; el subárbol
   en pie viaja rígidamente. Repetir. Si el proceso se atasca o una cara queda paralela al
   plano con bisagras imposibles, la configuración de cortes es inválida: **el despliegue es
   su propio oráculo de validez**.
6. **Render**: las figuras se dibujan en ASCII desde las posiciones finales de sus puntos.

## Nomenclatura paramétrica

Una instancia se nombra `P(a; c1·f1, ..., c6·f6)`: a = anclas por figura (2/3/4);
ci = cara (1 = apoyo); fi = figura según el catálogo (ver `catalogo_figuras.md`).
La instancia original es **P(2; 11, 2·90, 3·33, 44, 5·81, 6·80)**.

## Resultados verificados (computacionalmente)

- 384 árboles generadores del octaedro = 384 desarrollos etiquetados del cubo fijo.
- Los 384 completan el despliegue físico sin atasco y sin colisiones, con la base anclada.
- El oráculo de validez es exacto: de las 792 configuraciones de 5 aristas fijadas,
  completan exactamente las 384 válidas (0 falsos positivos, 0 falsos negativos).
- Módulo simetría del plano: 11 redes clásicas del cubo; con orientación fija: 64.
- La simulación física coincide con el mapa isométrico de desarrollo (tolerancia 1e-9)
  en las 384 configuraciones: el desarrollo del cubo es único y el proceso lo construye.

## Archivos

- `desarrollos_cubo_384.txt` — los 384 desarrollos anclados, con cortes y secuencias de plegado.
- `desarrollos_cubo_384_orientado.txt` — idem con los símbolos rotados según su base 2D.
- `catalogo_figuras.md` — catálogo paramétrico de figuras.
- `CITATION.cff` — metadatos de citación.

## Contexto

Los componentes son clásicos (redes de cubo conocidas desde Durero, 1525; tests de rotación
mental desde Vandenberg & Kuse, 1978; la novedad está en la integración: cubo etiquetado
fijo, reposando, con coherencia de orientación, como test paramétrico de estrés para IA.


---

## Convención visual del autor (formato canónico de exhibición)

El enunciado exige ASCII, y ASCII no rota glifos. La solución de exhibición, fijada por el autor:

- **Glifo erguido** como placeholder del símbolo + **flecha** indicando la orientación real
  que el símbolo debe tener en el plano (8 direcciones: ▲►▼◄↗↘↖↙).
- **Vértices (1)-(8) del cubo trackeados** por el desarrollo: cada etiqueta aparece tantas
  veces como copias materiales tiene el vértice tras el corte; la coherencia de etiquetas
  es condición necesaria y suficiente de validez (y su ruptura, demostración de imposibilidad).
- Las 11 redes tienen nombre de figura: TAU, TE, EQUIS, ZETA, ILATINA, SIETE, LANDA,
  IGRIEGA, EME, ESCALERA, ELE.

Configuración inicial (fijaciones) de la instancia documentada: A(base)→frente,
B(derecha)→diagonal techo-atrás, C(techo)→atrás, D(trasera)→diagonal techo-derecha,
E(izquierda)→techo, F(frente)→base. Recuperada por inversión de las flechas del documento
original: consistente en las 8 redes geométricamente determinadas.

## El problema en una frase

Sencillo de exponer, difícil de resolver, casi imposible de mostrar conforme a la
solicitud de ASCII. La triple tensión (enunciado / solución / exhibición) es el instrumento.
