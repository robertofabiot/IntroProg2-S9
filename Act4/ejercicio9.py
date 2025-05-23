# Separar pares e impares 
# Llena una lista con 10 números enteros aleatorios entre 1 y 100, y 
# sepáralos en dos listas: pares e impares. 

import random

lista = []

for i in range(10):
    lista.append(random.randint(1,100))

pares = []
impares = []

for i in range(10):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print(f"""
Pares: {pares}
Impares: {impares}
""")
