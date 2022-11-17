def suma(lista_numeros):
    suma = 0
    for i in lista_numeros:
        suma += i
    return suma


def multi(lista_numeros):
    multi = 1
    for i in lista_numeros:
        multi *= i
    return multi


print(suma([1, 2, 3, 4]))
print(multi([1, 2, 3, 4]))