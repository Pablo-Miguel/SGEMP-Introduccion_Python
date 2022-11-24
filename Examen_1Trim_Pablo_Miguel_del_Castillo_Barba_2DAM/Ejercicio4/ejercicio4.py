salir = False
while not salir:

    print("CATEGORIA          PRECIO             CODIGO             RECARGO/DIA DE ATRASO")
    print("FAVORITOS          2.50€                 1                     0.50€")
    print("NUEVOS             3.00€                 2                     0.75€")
    print("ESTRENOS           3.50€                 3                     1.00€")
    print("SUPER ESTRENOS     4.00€                 4                     1.50€")

    op_cod = str(input("Introduzca el codigo de la categoria de la película: "))
    op_dev = int(input("Introduzca el numero de dias de atraso en la devolucion: "))

    match op_cod:
        case "1":
            print(f"El total a pagar es: {round(2.5 + (op_dev * 0.5), 2)}€")
        case "2":
            print(f"El total a pagar es: {round(3.0 + (op_dev * 0.75), 2)}€")
        case "3":
            print(f"El total a pagar es: {round(3.5 + (op_dev * 1.0), 2)}€")
        case "4":
            print(f"El total a pagar es: {round(4.0 + (op_dev * 1.5), 2)}€")
        case _:
            print("Codigo incorrecto")

    op_salir = str(input("Si desea salir introduzca el 1 o de lo contrario presione otra tecla: "))
    if op_salir == "1":
        salir = True