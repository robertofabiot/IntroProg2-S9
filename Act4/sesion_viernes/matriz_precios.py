matriz = [[10.6, 2.8, 100], [300.98, 4.25, 125], [310, 1000, 8]]

print("Precios anteriores")
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6}", end = " |")
    print("|")
    print("-"*17)

while True:
    try:
        aumento = float(input("Ingrese el porcentaje a aumentar: "))
        if 0 >= aumento:
            raise TypeError
        break
    except TypeError:
        print("Ingrese un porcentaje mayor a 0")
aumento = (100+aumento)/100        

matriz_nueva = []

for fila in matriz:
    nueva_fila = []
    for columna in fila:
        nueva_fila.append(columna * 1.15)
    matriz_nueva.append(nueva_fila)

for fila in matriz_nueva:
    for columna in fila:
        print(f"|{columna:>6.2f}", end = " |")
    print("|")
    print("-"*17)

sumas = []

for fila in range(len(matriz)):
    nueva_fila = []
    for columna in fila:
        nueva_fila.append(matriz[fila[columna]]+matriz_nueva[fila[columna]])
    sumas.append(nueva_fila)