# Buscar un elemento
# Dada una lista de palabras, solicita al usuario una palabra y muestra si est� o no en la lista.

animales = ["perro", "gato", "cerdo", "vaca", "caballo"]

animal_buscado = input("Ingrese el animal que busca: ").lower()

if animal_buscado is animales:
    print("S� est�.")
else:
    print("No est�.")