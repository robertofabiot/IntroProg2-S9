# Invertir una lista 
# Pide 10 números al usuario, guárdalos en una lista e imprímelos en orden 
# inverso. 

lista = []

for i in range (10):
    numero_agregado = float(input("Ingrese un número"))
    lista.append(numero_agregado)

for i in range (9, -1, -1):
    numero_invertido = lista[i]
    del lista[i]
    lista.append(numero_invertido)

print(lista)
