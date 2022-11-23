class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def __str__(self):
        return f"Cuenta: [Titular: {self.titular}, cantidad: {self.cantidad}]"
