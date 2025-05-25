# 3. Control de inventario 
# Un almacén registra la cantidad de productos en 3 categorías diferentes, en 4 sucursales. 
# El programa debe: 
# • Usar una matriz 3x4. 
# • Calcular el total de productos por categoría. 
# • Mostrar cuál sucursal tiene el mayor inventario acumulado.

# Inventario
inventario = []

for fila in range(3):
    nueva_fila = []
    for columna in range(4):
        cant_productos = float(input(f"Ingrese la cantidad de productos de la categoría {fila} en la sucursal {columna}"))
        nueva_fila.append(cant_productos)
    inventario.append(nueva_fila)

# Total de productos por categoría
total_de_productos = []

for categoria in inventario:
    total_de_productos.append(sum(categoria))

print("TOTAL DE PRODUCTOS")
for i in range(len(total_de_productos)):
    print(f"Categoría {i+1}: {total_de_productos[i]}")

# Mostrar cual sucursal tiene el mayor inventario acumulado
totales_sucursales = [0] * 4 

for columna in range(4):
    for fila in range(3):
        totales_sucursales[columna] += inventario[fila][columna]

mayor = max(totales_sucursales)
indice_mayor = totales_sucursales.index(mayor)

print(f"\nLa sucursal con mayor inventario acumulado es la sucursal {indice_mayor} con un total de {mayor} productos.")