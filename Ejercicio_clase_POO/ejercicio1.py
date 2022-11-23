class Alumno:
    def __init__(self):
        self.__nombre: str = input("Introduzca el nombre del alumno: ")
        self.__nota: float = float(input("Introduzca la nota del alumno: "))

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, value):
        if 0 <= value <= 10:
            self.__nota = value
        else:
            print("La nota solo puede estar comprendida entre 0 y 10.\nNota actual: 0")
            self.__nota = 0

    def imprimir(self):
        print(self.__str__())

    def resultadoNota(self):
        if self.__nota >= 5:
            print(f"El alumno con nombre {self.__nombre}, ha aprobado con un {self.__nota}")
        else:
            print(f"El alumno con nombre {self.__nombre}, ha suspendido con un {self.__nota}")

    def __str__(self):
        return f"Alumno: [Nombre: {self.__nombre} , Nota: {self.__nota}]"


alumno1: Alumno = Alumno()
alumno1.imprimir()
alumno1.resultadoNota()
