while True:
    print("╔══════════════════════════════════════════════╗")
    print("║ 1.- Escribir tu nombre y mostrar en pantalla.║")
    print("║ 2.- Salir                                    ║")
    print("╚══════════════════════════════════════════════╝")

    opcion = input("\nElige una opción: ")
    if opcion == "2":
        break

    if opcion == "1":
        nombre = input("\nEscribe tu nombre: ")
        print(f"Hola {nombre}")
