def maximo(a, b):
    if a < b:
        return b
    elif b < a:
        return a
    else:
        print("Son iguales")
        return None

print(maximo(56, 123))