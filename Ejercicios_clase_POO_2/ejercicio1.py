from re import *

REGEXP = "[0-9]{8}[A-Z]"
DIGITO_CONTROL = "TRWAGMYFPDXBNJZSQVHLCKE"
INVALIDOS = {"00000000T", "00000001R", "99999999R"}
MAYOR_EDAD = 18


class Persona:

    def __init__(self,nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        if value < 0:
            print(f"Edad incorrecta. Edad actual: {self.__edad} años")
        else:
            self.__edad = value

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, value):
        if self.validar_dni(value):
            self.__dni = value
        else:
            print(f"DNI incorrecto. DNI actual: {self.__dni}")

    def validar_dni(self):
        return self.__dni not in INVALIDOS \
               and match(REGEXP, self.__dni) is not None \
               and self.__dni[8] == DIGITO_CONTROL[int(self.__dni[0:8]) % 23]

    def mostrar(self):
        print(self.__str__())

    def esMayorDeEdad(self):
        return self.__edad >= MAYOR_EDAD

    def __str__(self):
        return f"Persona: [Nombre: {self.__nombre}, Edad: {self.__edad} años, DNI: {self.__dni}]"