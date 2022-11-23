class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def imprimir(self):
        print(self.__str__())

    def __str__(self):
        return f"Titular: {self.titular}, cantidad: {self.cantidad}"

class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)

    def mostrar(self):
        print(self.__str__())

    def __str__(self):
        return f"Caja de ahorros: [{super().__str__()}]"

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def obtenerImporteInteres(self):
        return round(float(self.cantidad) * float(self.interes) / 100)
    def mostrar(self):
        print(self.__str__())
    def __str__(self):
        return f"Plazo fijo: [{super().__str__()}, plazo: {self.plazo}, interés: {self.interes}, total interés: {self.obtenerImporteInteres()}]"


cajaahorros: CajaAhorro = CajaAhorro("Pablo Miguel", 4000)
cajaahorros.mostrar()
plazoFijo: PlazoFijo = PlazoFijo("Marta", 5000, 5, 2)
plazoFijo.mostrar()
