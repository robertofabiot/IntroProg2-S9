# 4. Registro de temperaturas 
# Un sensor registra la temperatura cada hora durante 3 días (24h/día). 
# En el programa: 
# • Crear una matriz 3x24. 
# • Calcular temperatura máxima, mínima y promedio por día. 
# • Mostrar en qué hora se registró la temperatura más alta en cada día. 

import random

#Crear matriz
registro_temperatura = []

    #Ingresar temperaturas
for fila in range(3): 
    nueva_fila = []
    for columna in range(24):
        nueva_fila.append(round(random.uniform(-10,40), 2))
    registro_temperatura.append(nueva_fila)

#Calcular temperatura máxima, mínima y promedio por día
for fila in range(len(registro_temperatura)):
    temp_max_dia = max(registro_temperatura[fila])
    temp_min_dia = min(registro_temperatura[fila])
    temp_avg_dia = sum(registro_temperatura[fila])/len(registro_temperatura[fila])
    print(f"DÍA {fila+1}")
    print(f"La temperatura máxima fue {temp_max_dia:.2f} a las {registro_temperatura[fila].index(temp_max_dia)}")
    print(f"La temperatura mínima fue {temp_min_dia:.2f}")
    print(f"La temperatura promedio fue {temp_avg_dia:.2f}")