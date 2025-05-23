#Un docente desea registrar las calificaciones de sus 10 estudiantes en un examen.
#El programa debe:
#• Solicitar las calificaciones (sólo se permiten entre 0 a 100).
#• Mostrar el promedio, la calificación más alta, la más baja y cuántos aprobaron (>= 70).

lista = []

for i in range (10):
    while True:
        try:
            numero_agregado = float(input(f"Ingrese la calificación #{i+1}: "))
            if not(0 <= numero_agregado) & (numero_agregado <= 100):
                raise TypeError
            lista.append(numero_agregado)
            break
        except TypeError:
            print("Ingrese una calificación válida.")

aprobados = 0
for i in range(len(lista)):
    if lista[i] >= 70:
        aprobados += 1

print(f"La nota más alta es {max(lista)}")
print(f"La nota más baja es {min(lista)}") 
print(f"El promedio es {sum(lista)/len(lista)}")
print(f"Los aprobados fueron {aprobados}")