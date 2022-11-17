def es_palindromo(cadena):
    cadena.lower()
    return cadena.__eq__(cadena[::-1])


print(es_palindromo("radar"))