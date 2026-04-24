total_tiempo = 0

while True:
    print("\n--- Registro de actividades diarias ---")
    print("1. Registrar actividades")
    print("2. Mostrar análisis del tiempo")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        cantidad = int(input("Ingrese la cantidad de actividades (mínimo 3): "))

        while cantidad < 3:
            cantidad = int(input("Debe ingresar al menos 3 actividades: "))

        contador = 0

        while contador < cantidad:
            nombre = input("Ingrese el nombre de la actividad: ")
            tiempo = int(input("Ingrese el tiempo en minutos: "))

            total_tiempo += tiempo
            contador += 1

    elif opcion == 2:
        print("Tiempo total:", total_tiempo)

        if total_tiempo > 180:
            print("Tiempo diario excesivo")
        else:
            print("Tiempo diario adecuado")

    elif opcion == 3:
        print("Fin del registro")
        break

    else:
        print("Opción inválida")
