Algoritmo SmartEasyManager
	
    Dimension nombres[8]
    Dimension cantidades[8]
    Definir i Como Entero
	
    // Inicializar inventario
    nombres[1] <- "Parlantes"
    cantidades[1] <- 6
    nombres[2] <- "Micrófonos normales"
    cantidades[2] <- 4
    nombres[3] <- "Micrófonos inalámbricos"
    cantidades[3] <- 2
    nombres[4] <- "Pantallas"
    cantidades[4] <- 3
    nombres[5] <- "Proyectores"
    cantidades[5] <- 2
    nombres[6] <- "Luces robóticas"
    cantidades[6] <- 4
    nombres[7] <- "Luces LED"
    cantidades[7] <- 6
    nombres[8] <- "Consolas"
    cantidades[8] <- 2
	
    Definir opcion Como Entero
	
    Repetir
        Escribir "--- MENÚ PRINCIPAL ---"
        Escribir "1. Inventario"
        Escribir "2. Generar Cotización"
        Escribir "3. Salir"
        Escribir "Seleccione una opción: "
        Leer opcion
		
        Segun opcion Hacer
            1:
                MenuInventario(nombres, cantidades)
            2:
                GenerarCotizacion(dummy)
            3:
                Escribir "Gracias por usar Smart Easy Manager"
            De Otro Modo:
                Escribir "Opción no válida. Intente de nuevo."
        FinSegun
    Hasta Que opcion = 3
	
FinAlgoritmo

// ------------------- SUBPROCESO MENU INVENTARIO -------------------

SubProceso MenuInventario(nombres Por Referencia, cantidades Por Referencia)
    Definir subopcion, item, cantidad Como Entero
	
    Repetir
        Escribir "--- GESTIÓN DE INVENTARIO ---"
        Escribir "1. Ver Inventario"
        Escribir "2. Agregar unidades"
        Escribir "3. Quitar unidades"
        Escribir "4. Volver al menú principal"
        Escribir "Seleccione una opción:"
        Leer subopcion
		
        Segun subopcion Hacer
            1:
                MostrarInventario(nombres, cantidades)
            2:
                MostrarInventario(nombres, cantidades)
                Escribir "Seleccione el número del ítem a aumentar:"
                Leer item
                Escribir "¿Cuántas unidades desea agregar?"
                Leer cantidad
                cantidades[item] <- cantidades[item] + cantidad
                Escribir "Unidades agregadas correctamente."
            3:
                MostrarInventario(nombres, cantidades)
                Escribir "Seleccione el número del ítem a disminuir:"
                Leer item
                Escribir "¿Cuántas unidades desea quitar?"
                Leer cantidad
                Si cantidades[item] >= cantidad Entonces
                    cantidades[item] <- cantidades[item] - cantidad
                    Escribir "Unidades retiradas correctamente."
                Sino
                    Escribir "No hay suficientes unidades para retirar."
                FinSi
        FinSegun
    Hasta Que subopcion = 4
FinSubProceso

// ------------------- SUBPROCESO MOSTRAR INVENTARIO -------------------

SubProceso MostrarInventario(nombres, cantidades)
    Definir i Como Entero
    Escribir "--- INVENTARIO ACTUAL ---"
    Para i <- 1 Hasta 8
        Escribir i, ". ", nombres[i], ": ", cantidades[i]
    FinPara
FinSubProceso

// ------------------- SUBPROCESO COTIZACIÓN -------------------

SubProceso GenerarCotizacion(dummy)
    Definir horas Como Entero
    Definir necesitaDJ, necesitaMicrofonoEnVivo Como Caracter
    Definir total, equipo, transporte, tiempoExtra Como Real
	
    Escribir "--- GENERADOR DE COTIZACIÓN ---"
    Escribir "Ingrese cantidad de horas del evento:"
    Leer horas
	
    Escribir "¿Requiere DJ? (S/N):"
    Leer necesitaDJ
	
    Escribir "¿Requiere micrófonos para grupo en vivo? (S/N):"
    Leer necesitaMicrofonoEnVivo
	
    equipo <- 150
    transporte <- 50
    tiempoExtra <- 0
	
    Si necesitaDJ = "S" o necesitaDJ = "s" Entonces
        equipo <- equipo + 70
    FinSi
	
    Si necesitaMicrofonoEnVivo = "S" o necesitaMicrofonoEnVivo = "s" Entonces
        equipo <- equipo + 40
    FinSi
	
    Si horas > 6 Entonces
        tiempoExtra <- (horas - 6) * 25
    FinSi
	
    total <- equipo + transporte + tiempoExtra
	
    Escribir ""
    Escribir "--- COTIZACIÓN FINAL ---"
    Escribir "Categoría      | Precio ($)"
    Escribir "---------------------------"
    Escribir "Equipo         | ", equipo
    Escribir "Transporte     | ", transporte
    Escribir "Tiempo extra   | ", tiempoExtra
    Escribir "---------------------------"
    Escribir "TOTAL          | ", total
    Escribir "---------------------------"
FinSubProceso
