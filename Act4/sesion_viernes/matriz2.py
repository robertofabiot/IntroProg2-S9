#MATRIZ
matriz = [[10.6, 2.8], [300.98, 4.25]]
print("-"*17)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6.1f}", end = " |")
    print("|")
    print("-"*17)