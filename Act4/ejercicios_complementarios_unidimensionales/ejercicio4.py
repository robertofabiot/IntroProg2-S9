# 4. Registro de sueldos 
# Se registra el sueldo de 12 empleados. 
# El programa debe: 
# • Almacenar los sueldos. 
# • Calcular cuántos ganan más de $1,000. 
# • Hallar el sueldo promedio. 
# • Identificar si algún sueldo es exactamente $0 (posible error de captura).

sueldos = []

for i in range (12):
    numero_agregado = float(input("Ingrese un número: "))
    sueldos.append(numero_agregado)

#Calcular cuántos ganan más de $1,000. 
sueldo_mayor_1000 = 0
for sueldo in sueldos:
    if sueldo > 1000:
        sueldo_mayor_1000 += 1

#Hallar el sueldo promedio.
sueldo_promedio = sum(sueldos)/len(sueldos)

#Identificar si un sueldo es exactamente $0.
for i in range(len(sueldos)):
        if sueldos[i] == 0:
            print(f"El sueldo {i+1} es 0. Posible error de captura.")

print(f"La cantidad de empleados que ganan más de 1000 son {sueldo_mayor_1000}")
print(f"El sueldo promedio es {sueldo_promedio:.2f}")