#MATRIZ
matriz = [["Roberto", "Fabio", "Tercero"], ["Abril", "Milagros", "Tercero"], ["Roberto", "Antonio", "Tercero"]]
print("-"*17)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6}", end = " |")
    print("|")
    print("-"*17)
    
matriz_letras = []

for fila in matriz:
    nueva_fila = []
    for columna in fila:
            nueva_fila.append(len(columna))
    matriz_letras.append(nueva_fila)

for fila in matriz_letras:
    for columna in fila:
        print(f"|{columna:>6}", end = " |")
    print("|")
    print("-"*17)