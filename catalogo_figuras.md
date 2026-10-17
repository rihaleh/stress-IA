# Catálogo de figuras del problema paramétrico del cubo

## Convención de codificación

- Las figuras se numeran por bloques según su dimensión o número de lados/puntos.
- El número base es la figura en orientación **horizontal** (o única).
- Los sufijos numéricos declaran variantes de orientación o subtipo.
- El catálogo ES parte del enunciado: dos instancias solo son comparables si usan el mismo catálogo.
- Una instancia del problema se nombra: `P(a; c1·f1, c2·f2, ..., c6·f6)` donde `a` = nº de anclas por figura (2, 3 o 4), `ci` = cara (1-6; cara 1 = plano de apoyo) y `fi` = código de figura en este catálogo.

## 1. Figuras de 1 y 2 dimensiones (puntos y líneas) — FIJADO

| Código | Figura |
|---|---|
| 1 | Punto |
| 2 | Recta horizontal |
| 21 | Recta vertical |

## 2. Figuras de 3 lados (triángulos) — FIJADO

| Código | Figura |
|---|---|
| 3 | Triángulo isósceles horizontal |
| 31 | Triángulo isósceles vertical |
| 32 | Triángulo rectángulo, ángulo recto abajo derecha |
| 33 | Triángulo rectángulo, ángulo recto abajo izquierda |
| 34 | Triángulo rectángulo, ángulo recto arriba izquierda |
| 35 | Triángulo rectángulo, ángulo recto arriba derecha |

## 3. Figuras de 4 lados (cuadriláteros) — FIJADO

| Código | Figura |
|---|---|
| 4 | Cuadrado horizontal |
| 41 | Cuadrado vertical o rombo |

## 4. Figuras de n lados, polígonos regulares (n ≥ 5) — patrón FIJADO, tabla generada

| Código | Figura |
|---|---|
| 5 | Pentágono regular horizontal |
| 51 | Pentágono regular girado izquierda |
| 52 | Pentágono regular girado derecha |
| 6 | Hexágono regular horizontal |
| 61 | Hexágono regular girado izquierda |
| 62 | Hexágono regular girado derecha |
| 7 | Heptágono regular horizontal |
| 71 / 72 | Heptágono regular girado izquierda / derecha |
| 8 | Octógono regular horizontal |
| 81 / 82 | Octógono regular girado izquierda / derecha |
| 9 | Eneágono regular horizontal |
| 91 / 92 | Eneágono regular girado izquierda / derecha |
| 10 | Decágono regular horizontal |
| 101 / 102 | Decágono regular girado izquierda / derecha |
| 11 | Endecágono regular horizontal |
| 111 / 112 | Endecágono regular girado izquierda / derecha |
| 12 | Dodecágono regular horizontal |
| 121 / 122 | Dodecágono regular girado izquierda / derecha |

Patrón: para n ≥ 5, `n` = horizontal, `n1` = girado izquierda, `n2` = girado derecha.
El "giro" se define como media unidad central (para pentágono 36°), salvo declaración distinta en el enunciado.

## 5. Figuras especiales (no poligonales regulares) — PROPUESTA a ratificar

| Código | Figura | Notas |
|---|---|---|
| 80 | Estrella de 5 puntas horizontal | contorno de 10 vértices |
| 801 / 802 | Estrella girada izquierda / derecha | giro de 36° |
| 81 | Cruz alagada vertical | contorno de 12 vértices |
| 811 / 812 | Cruz alagada horizontal (girada) | |
| 82 | Cruz simétrica (greca simple) | si se desea distinguir de la alagada |

## 6. Figuras con curvas — PROPUESTA a ratificar

Regla de discretización: toda curva se aproxima por su polígono regular de n vértices,
con n múltiplo de 4 y n mayor que el máximo de vértices de las figuras poligonales presentes
(en este catálogo, la estrella manda con 10, luego n = 12).

| Código | Figura | Notas |
|---|---|---|
| 90 | Círculo | discretizado, n = 12 (múltiplo de 4) |
| 901 | Semicírculo, apertura arriba | |
| 902 | Semicírculo, apertura abajo | |
| 91 | Elipse horizontal | n par, declarado en el enunciado |
| 911 | Elipse vertical | |
| 92 | Arco de cuarto de círculo | |

## 7. Instancia canónica del problema original

Con este catálogo, el problema tal como se planteó en la conversación es:

**P(2; 11, 2·90, 3·33, 44, 5·81, 6·80)**

Anclaje 2. Cara 1 (apoyo): punto. Cara 2: círculo. Cara 3: triángulo rectángulo con ángulo
recto abajo izquierda. Cara 4: cuadrado horizontal. Cara 5: cruz alagada. Cara 6: estrella
de 5 puntas. Cubo fijo, reposando en el plano, sin levantarse; desarrollos por cortes de
aristas con las 6 caras conectadas; símbolos con coherencia de orientación respecto a la
configuración inicial.
