# 7. De una empresa de transporte se quiere guardar el nombre de los conductores que 
# tiene, y los kilómetros que conducen cada día de la semana. 
# Para guardar esta información se van a utilizar dos arreglos: 
# • Nombre: Vector para guardar los nombres de los conductores. 
# • kms: Tabla para guardar los kilómetros que realizan cada día de la semana. 
# Se quiere generar un nuevo vector (“total_kms”) con los kilómetros totales que realiza 
# cada conductor. 
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha 
# realizado. 

while True:
    try:
        n_filas = int(input("¿Cuántos conductores tiene la empresa?: "))
        if n_filas < 0:
            raise ValueError
        break
    except ValueError:
        print("Ingrese un número válido.")

nombre_kms = []

for fila in range(n_filas):
    nueva_fila = []
    for columna in range(8):
        if columna == 0:
            nombre = input("Ingrese el nombre del conductor: ")
            nueva_fila.append(nombre)
        else:
            while True:
                try:
                    kms = float(input(f"Ingrese los kms que hizo el día {columna}: "))
                    if kms < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Ingrese un número válido.")
            nueva_fila.append(kms)
    nombre_kms.append(nueva_fila)

# Kilómetros totales que realiza cada conductor.
total_kms = []

for fila in nombre_kms:
    total_kms.append(sum(fila[1:8]))

for conductor in range(len(nombre_kms)):
    print(f"El conductor {nombre_kms[conductor][0]} hizo {total_kms[conductor]}")