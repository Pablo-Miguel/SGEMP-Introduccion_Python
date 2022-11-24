class Contacto:
    def __init__(self):
        self.nombre = str(input("Introduzca nombre: "))
        self.telefono = str(input("Introduzca telefono: "))
        self.email = str(input("Introduzca email: "))


listaContactos = []

salir = False
while not salir:
    op_salir = str(input("¿Quieres introducir un contacto? (1 - Si, 2 - No): "))
    if(op_salir == "1"):
        contactoTemp = Contacto()
        listaContactos.append(contactoTemp)
        print("- Añadir contacto")
        print("- Lista de contacto")
        print("- Buscar contacto")
        print("- Editar contacto")
        print("- Cerrar contacto")
    else:
        salir = True