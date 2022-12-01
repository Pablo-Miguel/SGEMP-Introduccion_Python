from random import *

salir: bool = False

while not salir:
    try:

        cantidad_total: float = round(float(input("Introduzca la cantidad total de la compra: ")))

        if cantidad_total >= 100:
            print("Su gasto iguala o supera los 100.00€ y por tanto participa en la promocion.")
            print("            COLOR                              DESCUENTO                   ")
            print("         Bola blanca                            No tiene                   ")
            print("         Bola roja                             10 por ciento               ")
            print("         Bola azul                             20 por ciento               ")
            print("         Bola verde                            25 por ciento               ")
            print("         Bola amarilla                         50 por ciento               ")

            numero: int = randint(1, 5)

            match numero:
                case 1:
                    print("Aleatoriamente usted obtuvo una bola blanca")
                    print("Ohhhh, no tienes descuento")
                    print(f"Su nuevo total a pagar es: {cantidad_total}€")
                case 2:
                    print("Aleatoriamente usted obtuvo una bola roja")
                    print("Felicidades, ha ganado un 10 por ciento")
                    print(f"Su nuevo total a pagar es: {round(cantidad_total * 0.9, 2)}€")
                case 3:
                    print("Aleatoriamente usted obtuvo una bola azul")
                    print("Felicidades, ha ganado un 20 por ciento")
                    print(f"Su nuevo total a pagar es: {round(cantidad_total * 0.8, 2)}€")
                case 4:
                    print("Aleatoriamente usted obtuvo una bola verde")
                    print("Felicidades, ha ganado un 25 por ciento")
                    print(f"Su nuevo total a pagar es: {round(cantidad_total * 0.75, 2)}€")
                case 5:
                    print("Aleatoriamente usted obtuvo una bola amarilla")
                    print("Felicidades, ha ganado un 50 por ciento")
                    print(f"Su nuevo total a pagar es: {round(cantidad_total * 0.5, 2)}€")

        else:
            print("Su gasto NO supera los 100.00€ y por tanto NO participa en la promocion.")

        if input("Si desea salir introduzca el 1 o de lo contrario presione otra tecla: ") == "1":
            salir = True

    except:
        print("Has introducido caracteres erroneos")
        salir = True