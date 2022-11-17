def filtrar_palabras(lista, num):
    listaPalabras = []
    for cad in lista:
        if len(cad) >= num:
            listaPalabras.extend([cad])

    return listaPalabras


print(filtrar_palabras(["sa", "fdsf", "sad", "s", "asddfd", "ds"], 3))
