#Encuesta de satisfacci�n
#Un sistema de encuestas almacena las respuestas de 20 personas que valoran un 
#servicio del 1 al 5.
#El programa debe:
#� Almacenar las respuestas en una lista.
#� Contar cu�ntas personas eligieron cada puntuaci�n.
#� Mostrar el porcentaje de satisfacci�n (4 y 5).

lista = []

for i in range (20):
    numero_agregado = float(input("Ingrese un n�mero: "))
    lista.append(numero_agregado)

for i in range (1,6): #Recorre las puntuaciones posibles
    contador = 0
    for satisfaccion in range(20): #Recorre todas las puntuaciones
        if i == lista[satisfaccion]:
            contador += 1
    print(f"Puntuaci�n {i}: {contador}")        
        
print(f"El porcentaje de satisfacci�n es de {sum(lista)}%")
