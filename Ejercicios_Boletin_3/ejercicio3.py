print("COMPROBADOR DE RIMAS")

print("Introduzca la primera palabra:")
cadena1: str = input()

print("Introduzca la segunda palabra:")
cadena2:str = input()

if cadena1.endswith(cadena2[len(cadena2) - 3:]):
    print(f"La palabra {cadena1} rima con {cadena2}")
elif cadena1.endswith(cadena2[len(cadena2) - 2:]):
    print(f"La palabra {cadena1} rima un poco con {cadena2}")
else:
    print(f"Las palabras {cadena1} y {cadena2} no riman")