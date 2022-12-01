from ejercicio2 import *


class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, value):
        self.__bonificacion = value

    def esTitularValido(self):
        if 18 <= super().titular.edad <= 25:
            return True
        else:
            return False

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print(f"No eres un usuario válido")

    def mostrar(self):
        print(self.__str__())

    def __str__(self):
        return f"CuentaJoven: [{super().__str__()}, bonificación: {self.__bonificacion}%]"
