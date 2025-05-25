# 2. Tabla de resultados deportivos 
# Un equipo juega 5 partidos y registra goles anotados y recibidos. 
# En el programa: 
# • Crear una matriz 5x2 (columna 1: goles a favor, columna 2: goles en contra). 
# • Calcular el total de goles anotados, recibidos y diferencia de goles. 
# • Mostrar si el equipo ganó más partidos de los que perdió. 

#Registrar goles
goles = []

for fila in range(5):
    nueva_fila = []
    print(F"PARTIDO {fila+1}")
    for columna in range(2):
        if columna == 0:
            goles_partido = int(input("Ingrese la cantidad de goles anotados: "))
        elif columna == 1:
            goles_partido = int(input("Ingrese la cantidad de goles recibidos: "))
        nueva_fila.append(goles_partido)
    goles.append(nueva_fila)

#Calcular el total de goles anotados, recibidos y diferencia de goles. 
goles_anotados = goles_recibidos = 0

for fila in range(len(goles)):
    for columna in range(len(goles[fila])):
        if columna == 0:
            goles_anotados += (goles[fila])[columna]
        elif columna == 1:
            goles_recibidos += (goles[fila])[columna]
print("\n")

diferencia_goles = goles_anotados - goles_recibidos

print(f"Los goles anotados fueron {goles_anotados}")
print(f"Los goles recibidos fueron {goles_recibidos}")
print(f"La diferencia de goles fue de {diferencia_goles}")

#Mostrar si el equipo ganó más partidos de los que perdió
partidos_ganados = partidos_perdidos = empates = 0

for fila in goles:
    if fila[0] - fila[1] > 0:
        partidos_ganados += 1
    elif fila[0] - fila[1] < 0:
        partidos_perdidos += 1
    else:
        empates += 1

print(f"Los partidos ganados fueron {partidos_ganados}")
print(f"Los partidos perdidos fueron {partidos_perdidos}")
print(f"Los empates fueron {empates}")

if partidos_ganados > partidos_perdidos:
    print("Hubieron más victorias que derrotas.")
elif partidos_ganados < partidos_perdidos:
    print("Hubieron más derrotas que victorias.")
else:
    print("Todos fueron empates.")