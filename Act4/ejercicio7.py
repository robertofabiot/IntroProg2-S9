# Encontrar el máximo y el mínimo 
# A partir de una lista de números reales, encuentra el mayor y el menor 
# valor. 

lista = []

for i in range (10):
    numero_agregado = float(input("Ingrese un número: "))
    lista.append(numero_agregado)

for i in range (10):
    if i == 0:
        numero_mayor = lista[i] 
        numero_menor = lista[i]
    else:
        if numero_mayor < lista[i]:
            numero_mayor = lista[i]
        if numero_menor > lista[i]:
            numero_menor = lista[i]

print(f"""
Numero mayor: {numero_mayor}
Numero menor: {numero_menor}
""") 
