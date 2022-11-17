print("Ingrese una cadena: ")
cadena = input()

contMayus = 0
for car in cadena:
    if car.isupper():
        contMayus+=1

print("La cadena " + cadena + " tiene " + str(contMayus) + " mayúsculas")