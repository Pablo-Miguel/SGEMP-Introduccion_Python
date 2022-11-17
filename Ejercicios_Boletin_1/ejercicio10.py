import ejercicio9 as ej9

def procedimiento(lista_numeros):
    for i in lista_numeros:
        print(str(i) + ": " + ej9.generar_n_caracteres(i, '*'))


procedimiento([4, 9, 7])