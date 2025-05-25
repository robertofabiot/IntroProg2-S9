# 1. Registro de calificaciones por materia 
# Un estudiante registra sus calificaciones en 4 materias durante 3 parciales. 
# En el programa: 
# • Usar una matriz 4x3. 
# • Calcular el promedio de cada materia. 
# • Mostrar la calificación más alta de toda la matriz. 

calificaciones = []

#Usar una matriz 4x3. 
for fila in range(4):
    nueva_fila = []
    for columna in range(3):
        calificacion = float(input(f"Materia #{fila+1}, parcial #{columna+1}: "))
        nueva_fila.append(round(calificacion, 2))
    calificaciones.append(nueva_fila)

#Calcular el promedio de cada materia
i = 0
for fila in calificaciones:
    print(f"El promedio de la materia {i+1} es {sum(fila)/len(fila)}")
    i += 1

#Mostrar la calificación más alta de toda la matriz. 
print(f"La nota más alta fue {max(max(calificaciones))}")