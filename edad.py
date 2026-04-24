print("--- Registro de actividades diarias ---")

opcion = 0
tiempo_total = 0

while opcion != 3:

    print("\n1. Registrar actividades")
    print("2. Mostrar tiempo total")
    print("3. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:

        tiempo_total = 0  # reinicia cada vez

        cantidad = int(input("Ingrese cantidad de actividades (mínimo 3): "))

        while cantidad < 3:
            cantidad = int(input("Debe ser mínimo 3: "))

        contador = 0

        while contador < cantidad:
            actividad = input("Nombre: ")
            tiempo = int(input("Tiempo en minutos: "))

            tiempo_total = tiempo_total + tiempo
            contador = contador + 1

    elif opcion == 2:
        
        print("Tiempo total:", tiempo_total)
        if tiempo_total > 180:
            print("Tiempo excesivo")
        else:
            print("Tiempo adecuado")
        

    elif opcion == 3:
        print("Fin")

    else:
        print("Opción inválida")