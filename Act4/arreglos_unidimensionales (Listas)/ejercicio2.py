# Sumar los elementos de una lista
# Solicita 10 números al usuario, guárdalos en una lista y muestra la suma total

lista = []

for i in range(10):
    numero_añadido = int(input("Ingrese el número a añadir a la suma."))
    lista.append(numero_añadido)

print(f"La suma es {sum(lista)}.")