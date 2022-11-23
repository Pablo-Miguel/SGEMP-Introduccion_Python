class Calculadora:
    def __init__(self):
        self.num1 = float(input("Introduzca el num1: "))
        self.num2 = float(input("Introduzca el num2: "))

    def suma(self):
        print(f"Suma: {self.num1} + {self.num2} = {round(self.num1 + self.num2, 2)}")

    def resta(self):
        print(f"Resta: {self.num1} - {self.num2} = {round(self.num1 - self.num2, 2)}")

    def multiplicacion(self):
        print(f"Multiplicacion: {self.num1} * {self.num2} = {round(self.num1 * self.num2, 2)}")

    def division(self):
        print(f"Division: {self.num1} / {self.num2} = {round(self.num1 / self.num2, 2)}")


calculadora1: Calculadora = Calculadora()
calculadora1.suma()
calculadora1.resta()
calculadora1.multiplicacion()
calculadora1.division()