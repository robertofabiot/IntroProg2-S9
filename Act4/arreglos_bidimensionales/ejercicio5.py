# 5. Diseñar el programa que permita: 
# • Crear una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’. 
# • Carga la tabla de forma que los componentes pertenecientes a la diagonal de la 
# matriz tomen el valor 1 y el resto el valor 0. 
# • Muestra el contenido de la tabla en pantalla.

diagonal = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

i = 0
for fila in diagonal:
    (diagonal[i])[i] += 1
    i += 1

for fila in diagonal:
    print(fila)