# 5. Contar elementos mayores que un n�mero
# Dada una lista de 10 n�meros, contar cu�ntos son mayores que 50

lista = []

for i in range(10):
    numero_anadido = int(input("Ingrese el n�mero."))
    lista.append(numero_anadido)

contador = 0

for numero in lista:
    if numero > 50:
        contador += 1
    
print(f"Los n�meros mayores a 50 son {contador}")