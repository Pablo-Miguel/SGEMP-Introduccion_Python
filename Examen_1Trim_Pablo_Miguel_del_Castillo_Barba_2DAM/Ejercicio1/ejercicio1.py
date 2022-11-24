from random import *

print("Mastermind")

op_long = int(input("Dime la longitud de la cadena: "))

numero = ""

for pos, num in enumerate(range(op_long)):
    if pos == 0:
        numero += str(randint(1, 9))
    else:
        numero += str(randint(0, 9))

#print(f"NUMERO GANADOR: {numero}")

salir = False
cont = 0
while not salir:
    op_adv = str(input("Intenta adivinar la cadena: "))

    if len(op_adv) == len(numero):
        if op_adv != numero:
            for pos, car in enumerate(op_adv):
                if car == numero[pos]:
                    cont += 1
            print(f"Con {op_adv} has adivinado {cont} valores")
            cont = 0
        elif op_adv == numero:
            print(f"Con {op_adv} has adivinado {len(numero)} valores")
            print("Felicidades")
            salir = True
    else:
        print("Has metido un valor incorrecto")
        salir = True
