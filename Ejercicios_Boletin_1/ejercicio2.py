def max_de_tres(a, b, c):
    lista = [a, b, c]
    lista.sort()
    lista.reverse()
    return lista[0]

print(max_de_tres(32, 563, 123))
