def isVocal(caracter):
    caracter.lower()
    match caracter:
        case 'a':
            return True
        case 'e':
            return True
        case 'i':
            return True
        case 'o':
            return True
        case 'u':
            return True
        case _:
            return False


print(isVocal('g'))
