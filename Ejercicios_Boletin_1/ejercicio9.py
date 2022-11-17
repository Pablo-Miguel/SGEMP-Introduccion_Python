def generar_n_caracteres(num, caracter):
    cadena = ""
    for i in range(num):
        cadena += caracter
    return cadena


#print(generar_n_caracteres(5, 'X'))