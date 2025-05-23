# 3. Total de ventas diarias
# Una tienda registra sus ventas durante los 7 días de la semana.
# En el programa se debe:
# • Ingresar los montos de venta diaria.
# • Calcular el total y el promedio semanal.
# • Mostrar qué día tuvo mayor y menor venta

# Total de ventas diarias
# Una tienda registra sus ventas durante los 7 días de la semana.
# En el programa se debe:
# • Ingresar los montos de venta diaria.
# • Calcular el total y el promedio semanal.
# • Mostrar qué día tuvo mayor y menor venta

#Crear matriz para printear días
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

#Crear la lista con los montos de venta diaria
lista = []
for i in range (7):
    numero_agregado = float(input(f"Ingrese la venta del {dias[i]}: "))
    lista.append(numero_agregado)

#Calcular el total, promedio semanal, mayor y menor venta
total = sum(lista)
promedio = total/len(lista)
mayor_venta = max(lista)
menor_venta = min(lista)

#Encontrar mayor y menor venta
for i in range(len(lista)):
    if mayor_venta == lista[i]:
        dia_mayor_venta = dias[i]

for i in range(len(lista)):
    if menor_venta == lista[i]:
        dia_menor_venta = dias[i]

#Imprimir resultados
print(f"""
Total: {total:.2f}
Promedio de la semana: {promedio:.2f}
Día de mayor venta: {dia_mayor_venta} con {mayor_venta:.2f}
Día de menor venta: {dia_menor_venta} con {menor_venta:.2f}
""")