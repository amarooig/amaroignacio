print(f"¿que vas a beber?")

while True:
    print("1. coca-cola\n2. sprite\n3. fanta\n4. salir")
    elegiste = int(input("elige tu bebida favorita: "))

    if elegiste == 1:
        print("coca-cola? muy buena eleccion¡¡¡¡")
    elif elegiste == 2:
        print("vas a beber sprite? Que refrescante¡¡¡¡")
    elif elegiste == 3:
        print("mmmm fanta? bueno, gustos son gustos.")    
    else:
        print("elige una opcion valida")    
    
    break
    