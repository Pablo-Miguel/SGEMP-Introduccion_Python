class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: [Nombre: {self.nombre}, edad: {self.edad} años]"

    def mostrar(self):
        print(self.__str__())

    def mayorEdad(self):
        if self.edad >= 18:
            print(f"La persona {self.nombre} es mayor de edad, con {self.edad} años")
        else:
            print(f"La persona {self.nombre} es menor de edad, con {self.edad} años")


pers: Persona = Persona("Pablo Miguel", 19)
pers.mostrar()
pers.mayorEdad()