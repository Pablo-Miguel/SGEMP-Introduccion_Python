class Alumno:
    def __init__(self):
        self.nombre: str = input("Introduzca el nombre del alumno: ")
        self.nota: float = float(input("Introduzca la nota del alumno: "))

    def __str__(self):
        return f"Alumno: [Nombre: {self.nombre} , Nota: {self.nota}]"

    def imprimir(self):
        print(self.__str__())

    def resultadoNota(self):
        if self.nota >= 5:
            print(f"El alumno con nombre {self.nombre}, ha aprobado con un {self.nota}")
        else:
            print(f"El alumno con nombre {self.nombre}, ha suspendido con un {self.nota}")


alumno1: Alumno = Alumno()
alumno1.imprimir()
alumno1.resultadoNota()
