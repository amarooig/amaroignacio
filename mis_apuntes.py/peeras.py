vengadores = ["iron-man", "thor", "capitan america", "spider-man"]

while True:
    print (f"---Menu Vengadores---\n 1-Agregar Avenger\n 2-Mostrar Base y Modificar\n 3-Salir.")
    escoja = int(input("selecione un menu:"))
    if escoja == 1:
         nuevo_vengador = (input("agrega a un avenger:"))
         vengadores.append(nuevo_vengador)
         print(f"bienvenido {nuevo_vengador} a los avengers")
    elif escoja == 2:
        print("Lista de vengadores")

    for vengador in vengadores:
        print(vengador)

    print(f"\nTotal: {len(vengadores)} vengadores")