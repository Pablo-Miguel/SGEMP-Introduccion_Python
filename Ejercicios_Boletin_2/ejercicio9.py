def isVocal(vocal):
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        return True
    else:
        return False

def contar_vocales(palabra):
    print("Introduzca vocal a contar:")
    vocal = input()
    vocal.lower()
    if not(isVocal(vocal)):
        print("No es una vocal")
    else:
        match vocal:
            case "a":
                print(f"A: {sum(isVocal(x) and x == 'a' for x in palabra)}")
            case "e":
                print(f"E: {sum(isVocal(x) and x == 'e' for x in palabra)}")
            case "i":
                print(f"I: {sum(isVocal(x) and x == 'i' for x in palabra)}")
            case "o":
                print(f"O: {sum(isVocal(x) and x == 'o' for x in palabra)}")
            case "u":
                print(f"U: {sum(isVocal(x) and x == 'u' for x in palabra)}")
            case _:
                print("ERROR")


print("Introduzca una palabra:")
contar_vocales(str(input()))