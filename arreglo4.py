import os
import random
import time

participantes = list()
while True:
    os.system("cls||clear")
    os.system("color a1")
    nombre = input("Ingrese el nombre del participante (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    participantes.append(nombre.upper())
    print("Participante agregado...")
    print(participantes)
    
os.system("cls||clear")
print("Participantes Registrados")
print(participantes)
x = input("Presiona enter...")

for i in range(10, 0, -1):
    os.system("cls||clear")
    print(i)
    time.sleep(1)

fin = len(participantes) - 1
ganador = random.randint(0, fin)
print(f"Ganador: {participantes[ganador]}")