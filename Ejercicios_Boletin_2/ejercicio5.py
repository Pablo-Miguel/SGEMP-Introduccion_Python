def binario_a_entero(numero_binario):
    numero_decimal = 0

    for pos, num in enumerate(str(numero_binario)[::-1]):
        numero_decimal += int(num) * 2 ** pos

    return numero_decimal


print(binario_a_entero(101011100011101))