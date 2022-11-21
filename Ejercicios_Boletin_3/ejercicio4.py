print("CONVERTIDOR DE CAPITAL")

print("Introduzca una cantidad en dólares:")
dolares:float = float(input())

print("Introduzca una tasa de interés:")
tasa_interes:float = float(input())

print("Introduzca los años:")
anos:int = int(input())

resultado:float = (dolares * ((1 + (tasa_interes/100)) ** anos))
print(f"Una cantidad de {round(dolares, 2)}$ al {round(tasa_interes, 2)}% de interés anual se convierte en {round(resultado, 2)}$ al cabo de {anos} años")