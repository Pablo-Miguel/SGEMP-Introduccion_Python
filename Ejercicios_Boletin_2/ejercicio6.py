NUM_PERSONAS = 3

#
# CLASE PERSONA
#
class Persona:
    def __init__(self, nombre, nacimiento):
        self.nombre = nombre
        self.nacimiento = nacimiento


#
# ALGORITMO
#
print("Ingrese año en curso:")
ano_curso = input();

listaPersonas = []
for i in range(NUM_PERSONAS):
    print(f"Introduzca nombre de la persona {i + 1}")
    nombre = input()
    print(f"Introduzca año de nacimiento de la presona {i + 1}")
    nacimiento = input()
    listaPersonas.extend([Persona(str(nombre), int(nacimiento))])

print(f"AÑOS CUMPLIDOS DURANTE EL AÑO {ano_curso}")
for pos, pers in enumerate(listaPersonas):
    print(f"La persona {pos + 1}, con nombre: {pers.nombre} cumple {int(ano_curso) - int(pers.nacimiento)} años")