# 🧮 Programa de Listas Anidadas Interactivo

Este proyecto, desarrollado por **Joseph Alexander Morales Cardona**, es un programa en Python que permite al usuario **ingresar datos en una matriz** (listas anidadas) y realizar diferentes **operaciones interactivas** sobre ella utilizando **listas por comprensión**.

---

## 🚀 Descripción General

El programa guía al usuario paso a paso para:
1. Ingresar una cantidad de filas y columnas.
2. Introducir los datos de cada posición (pueden ser números o texto).
3. Procesar esa información con **listas por comprensión** para realizar operaciones como:
   - Aplanar la matriz.  
   - Filtrar solo números.  
   - Calcular sumas por fila (si todos los datos son numéricos).  
   - Transponer la matriz.  
   - Mostrar elementos únicos.  
   - Filtrar elementos por tipo (numérico, texto o todos).  
   - Contar la frecuencia de cada elemento.  
   - Generar combinaciones entre las dos primeras filas.

El código está pensado para **aprender y practicar conceptos de listas anidadas, comprensión de listas, estructuras de datos dinámicas y manipulación básica de matrices.**

---

## 🧩 Ejemplo de Uso

=== PROGRAMA DE LISTAS ANIDADAS INTERACTIVO ===
Ingresa datos y verás cómo se procesan con listas por comprensión anidadas

¿Cuántas filas de datos quieres ingresar? 2
¿Cuántas columnas tendrá cada fila? 3

Ingresa los datos fila por fila:
Fila 1, Columna 1: 1
Fila 1, Columna 2: 2
Fila 1, Columna 3: 3
Fila 2, Columna 1: a
Fila 2, Columna 2: b
Fila 2, Columna 3: c

=== MATRIZ INGRESADA ===
Fila 1: [1, 2, 3]
Fila 2: ['a', 'b', 'c']

=== OPERACIONES CON LISTAS ANIDADAS ===

1. Lista aplanada: [1, 2, 3, 'a', 'b', 'c']
2. Solo números: [1, 2, 3]
3. No se pueden hacer operaciones matemáticas (hay strings)

5. Elementos únicos: [1, 2, 3, 'a', 'b', 'c']
6. Filtrar elementos:
   ¿Qué tipo de elementos quieres ver? (num/texto/todos): texto
   Resultado: ['a', 'b', 'c']

7. Frecuencia de elementos:
   1: 1 veces
   2: 1 veces
   3: 1 veces
   a: 1 veces
   b: 1 veces
   c: 1 veces

8. Combinaciones entre filas:
   Combinaciones fila 1 con fila 2: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), ...]
MIT License

Copyright (c) 2025 Joseph Alexander Morales Cardona

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
