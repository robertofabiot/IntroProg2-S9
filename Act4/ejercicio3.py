# Promedio de calificaciones
# Solicita al usuario 8 calificaciones, gu�rdalas en una lista y calcula el promedio.

calificaciones = []

for i in range(8):
    calificacion = int(input(f"Ingrese la calificaci�n #{i+1}"))
    calificaciones.append(calificacion)

print(f"El promedio es {sum(calificaciones)/len(calificaciones)}")