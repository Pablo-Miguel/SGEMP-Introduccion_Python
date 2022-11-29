from ejercicio1 import *

class Cuenta:

    def __init__(self, titular = Persona(), cantidad = 0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, value):
        self.__titular = value

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, value):
        self.__cantidad = value

    def mostrar(self):
        print(self.__str__())

    def __str__(self):
        return f"Cuenta: [Titular: {self.__titular.__str__()}, cantidad: {self.__cantidad}]"

    def ingresar(self, cantidad):
        if cantidad < 0:
            print("No se puede ingresar una cantidad negativa")
        else:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad < 0:
            print("Cantiadad negativa, ingrese un número positivo a restar")
        else:
            self.__cantidad -= cantidad
