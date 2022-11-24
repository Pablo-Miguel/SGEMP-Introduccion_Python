
salir = False
while not salir:

    print("PRODUCTO                   CODIGO")
    print("CAMISA........................1")
    print("CINTURON......................2")
    print("ZAPATOS.......................3")
    print("PANTALON......................4")
    print("CALCETINES....................5")
    print("FALDAS........................6")
    print("GORRAS........................7")
    print("SUETER........................8")
    print("CORBATA.......................9")
    print("CHAQUETA......................10")

    op_cod = int(input("Introduzca codigo: "))
    precio = 0.0
    if 1 <= op_cod <= 5:
        precio = 10.0
    elif  6 <= op_cod <= 10:
        precio = 20.0
    else:
        print("Codigo incorrecto")
        precio = -1

    if precio != -1:
        print(f"El precio es: {precio}€")
        op_unidades = int(input("Introduzca numero de unidades: "))
        print(f"El total a pagar es: {round(precio * op_unidades, 2)}€")

    op_salir = str(input("Si desea salir introduzca el 1 o de lo contrario presione otra tecla: "))
    if op_salir == "1":
        salir = True