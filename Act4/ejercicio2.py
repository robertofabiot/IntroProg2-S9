# Sumar los elementos de una lista
# Solicita 10 n�meros al usuario, gu�rdalos en una lista y muestra la suma total

lista = []

for i in range(10):
    numero_a�adido = int(input("Ingrese el n�mero a a�adir a la suma."))
    lista.append(numero_a�adido)

print(f"La suma es {sum(lista)}.")