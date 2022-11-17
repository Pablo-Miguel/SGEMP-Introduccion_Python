NUM_PERSONAS = 10
EDAD_SUPERIOR = 20

listaEdades = []

for i in range(NUM_PERSONAS):
    print(f"Introduzca edad para la persona {i + 1}")
    listaEdades.extend([int(input())])

print(f"CANTIDAD PERSONAS SUPEROR A {EDAD_SUPERIOR} AÑOS")
# Count
# count = sum(func(x) for x in enumerable)
print(sum(x >= 20 for x in listaEdades))