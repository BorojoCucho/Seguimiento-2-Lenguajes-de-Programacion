# EJEMPLOS DE LISTAS POR COMPRENSIÓN ANIDADAS
"""
Las listas por comprensión son una forma elegante de crear listas en Python.
Pueden incluir:
1. Una expresión que define cada elemento
2. Un bucle for que itera sobre una secuencia
3. Condiciones opcionales (filtros)

Sintaxis básica: [expresión for elemento in secuencia if condición]
"""

# Ejemplo 1: Lista por comprensión simple para crear matriz de productos
# Versión expandida del código:
productos = []
for i in range(3):
    nombre = input(f"Producto {i+1}: ").strip()
    # validar precio: reintentar hasta que sea entero no-negativo
    while True:
        try:
            precio = int(input("Precio $: "))
            if precio < 0:
                print("El precio no puede ser negativo. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Precio inválido. Introduce un número entero.")
    # validar cantidad: reintentar hasta que sea entero >= 0
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Cantidad inválida. Introduce un número entero.")
    productos.append([nombre, precio, cantidad])

# Ejemplos adicionales de listas por comprensión:
print("\n=== EJEMPLOS DE LISTAS POR COMPRENSIÓN ===")
print("Lista original de productos:", productos)

# Ejemplo 2: Lista por comprensión con filtro
print("\n--- Ejemplos de filtrado ---")
caros = [p[0] for p in productos if p[1] > 100]  # Filtro simple
print("Productos caros:", caros)

# Ejemplo 3: Lista por comprensión con cálculos
print("\n--- Ejemplos de cálculos ---")
subtotales = [p[1] * p[2] for p in productos]  # Cálculo simple
print("Subtotales:", subtotales)

# Ejemplo 4: Lista por comprensión con múltiples condiciones
print("\n--- Ejemplos con múltiples condiciones ---")
productos_especiales = [p[0] for p in productos if p[1] > 100 and p[2] < 10]
print("Productos caros con poco stock:", productos_especiales)

# Ejemplo 5: Lista por comprensión con transformación
print("\n--- Ejemplos de transformación ---")
formato_producto = [f"{p[0]}: ${p[1]} x {p[2]} unidades" for p in productos]
print("Productos formateados:", formato_producto)

print("\n=== ANÁLISIS DE INVENTARIO ===")
print("1. Datos originales:", productos)
# [p[0] for p in productos] es una lista por comprensión que extrae solo los nombres
print("2. Nombres:", [p[0] for p in productos])
# [p[1]*p[2] for p in productos] calcula el subtotal de cada producto
print("3. Subtotales:", [p[1] * p[2] for p in productos])
# sum() con una lista por comprensión calcula el total del inventario
print("4. Total inventario: $", sum(p[1] * p[2] for p in productos))
# Lista por comprensión con filtro para productos caros
print("5. Productos con precio > $100:", [p[0] for p in productos if p[1] > 100])
# Lista por comprensión con filtro para stock bajo
print("6. Stock bajo (cantidad < 10):", [p[0] for p in productos if p[2] < 10])