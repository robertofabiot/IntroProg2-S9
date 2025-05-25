# 5. Análisis de números aleatorios 
# Se desea analizar una muestra de 30 números aleatorios entre 1 y 100. 
# En el programa se debe: 
# • Generar los números y almacenarlos. 
# • Separar los pares e impares en listas distintas. 
# • Mostrar la suma total de cada grupo y cuántos elementos contiene cada uno.

#Generar los números y almacenarlos
import random

lista = []
for i in range(30):
    lista.append(random.randint(1, 100))

#Separar los pares e impares en listas distintas
pares = []
impares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

#Mostrar la suma total de cada grupo y cuántos elementos contiene cada uno.
print(f"La suma de los pares es {sum(pares)} y contiene {len(pares)} elementos.")
print(f"La suma de los pares es {sum(impares)} y contiene {len(impares)} elementos.")