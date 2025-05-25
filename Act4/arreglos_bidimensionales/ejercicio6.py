# 6. Escribe un programa para: 
# • Crear una tabla bidimensional de longitud 5x15 y nombre ‘marco’. 
# • Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las 
# posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras 
# que el resto de los elementos contendrán el valor 0. 

marco = []

for fila in range(5):
    nueva_fila = []
    for columna in range(15):
        if fila in (0, 4) or columna in (0, 14):
            nueva_fila.append(1)
        else:
            nueva_fila.append(0)
    marco.append(nueva_fila)

for fila in marco:
    print(fila)