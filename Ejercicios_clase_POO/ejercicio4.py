class Banco:
    def __init__(self, clientes: list):
        self.clientes = clientes

    def operar(self):
        print("Seleccione numero del cliente:")
        for pos, cli in enumerate(self.clientes):
            print(f"Cliente {pos + 1}: {cli.nombre}")

        opcion: int = int(input())
        if self.clientes[opcion - 1] != None:
            cli: Cliente = self.clientes[opcion - 1]
            print(f"Bienvenido cliente {cli.nombre}.")
            operacion = input("Seleccione depositar -> d o extraer -> e: ")
            operacion.lower()
            if operacion.startswith("d"):
                cli.depositar()
            else:
                cli.extraer()

    def deposito_total(self):
        total = 0.0
        for cli in self.clientes:
            total += cli.cantidad
        print(f"Depósito total del banco: {total}€")

class Cliente:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = round(float(cantidad), 2)

    def depositar(self):
        self.cantidad += round(float(input("Introduzca canitdad a depositar: ")), 2)
        self.mostrar_total()

    def extraer(self):
        self.cantidad -= round(float(input("Introduzca canitdad a extraer: ")), 2)
        self.mostrar_total()

    def mostrar_total(self):
        print(f"Saldo actual: {self.cantidad}€")

    def __str__(self):
        return f"Cliente: [Nombre: {self.nombre}, Cantidad: {self.cantidad}]"


banco: Banco = Banco([Cliente("Pablo", 5000), Cliente("Marta", 2000), Cliente("Manu", 1000)])

banco.deposito_total()
banco.operar()
banco.deposito_total()