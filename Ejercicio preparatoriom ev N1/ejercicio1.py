
# 1. Inicializamos la variable con un valor que no sea el de salida
opcion = 0

# 2. El bucle se ejecuta mientras NO elijan la opción 3
while opcion != 3:
    print("--- MI PROGRAMA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    
    # 3. Pedimos la opción al usuario (convertida a entero)
    opcion = int(input("Elige una opcion: "))
    
    # 4. Evaluamos la opción elegida
    if opcion == 1:
        print("Elegiste Sumar")
    elif opcion == 2:
        print("Elegiste Restar")
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        # Si no es ninguna de las anteriores
        print("Opcion no valida, intenta de nuevo")

print("Programa finalizado con exito.")
