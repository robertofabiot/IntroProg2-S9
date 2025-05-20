# 5. Contar elementos mayores que un número
# Dada una lista de 10 números, contar cuántos son mayores que 50

lista = []

for i in range(10):
    numero_añadido = int(input("Ingrese el número."))
    lista.append(numero_añadido)

contador = 0

for numero in lista:
    if numero > 50:
        contador += 1
    
print(f"Los números mayores a 50 son {contador}")    