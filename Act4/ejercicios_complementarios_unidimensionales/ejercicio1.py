#Un docente desea registrar las calificaciones de sus 10 estudiantes en un examen.
#El programa debe:
#� Solicitar las calificaciones (s�lo se permiten entre 0 a 100).
#� Mostrar el promedio, la calificaci�n m�s alta, la m�s baja y cu�ntos aprobaron (>= 70).

lista = []

for i in range (10):
    while True:
        try:
            numero_agregado = float(input(f"Ingrese la calificaci�n #{i+1}: "))
            if not(0 <= numero_agregado) & (numero_agregado <= 100):
                raise TypeError
            lista.append(numero_agregado)
            break
        except TypeError:
            print("Ingrese una calificaci�n v�lida.")

aprobados = 0
for i in range(len(lista)):
    if lista[i] >= 70:
        aprobados += 1

print(f"La nota m�s alta es {max(lista)}")
print(f"La nota m�s baja es {min(lista)}") 
print(f"El promedio es {sum(lista)/len(lista)}")
print(f"Los aprobados fueron {aprobados}")