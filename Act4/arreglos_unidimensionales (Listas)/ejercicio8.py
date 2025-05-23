# Eliminar duplicados 
# Dada una lista con valores repetidos, crea una nueva lista sin duplicados. 

lista = []

for i in range (10):
    numero_agregado = float(input("Ingrese un número: "))
    lista.append(numero_agregado)

lista_nueva = []

for i in range (10):
    if lista[i] not in lista_nueva:
        lista_nueva.append(lista[i])

print(lista_nueva)