# Sumar elementos en posiciones pares 
# Suma los elementos que se encuentran en posiciones pares de la lista. 

lista = []

for i in range (10):
    numero_agregado = float(input("Ingrese un número: "))
    lista.append(numero_agregado)

suma_pares = 0

for i in range (10):
    if i % 2 == 0:
        suma_pares += lista[i]

print(f"La suma de los números en posiciones pares es {suma_pares}")