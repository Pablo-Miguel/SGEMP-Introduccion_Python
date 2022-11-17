def mas_larga(lista):
    max_cad = ""
    for cad in lista:
        if len(cad) > len(max_cad):
            max_cad = cad

    return max_cad


print(mas_larga(["a", "aaa", "asd", "dsfsd", "sa", "sasd"]))