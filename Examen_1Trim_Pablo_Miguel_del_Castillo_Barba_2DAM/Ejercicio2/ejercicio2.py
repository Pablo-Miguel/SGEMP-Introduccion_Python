class Triangulo:
    def __init__(self):
        self.l1 = round(float(input("Introduzca el valor para el lado 1: ")), 2)
        self.l2 = round(float(input("Introduzca el valor para el lado 2: ")), 2)
        self.l3 = round(float(input("Introduzca el valor para el lado 3: ")), 2)
        self.a1 = round(float(input("Introduzca el valor para el angulo 1: ")), 2)
        self.a2 = round(float(input("Introduzca el valor para el angulo 2: ")), 2)
        self.a3 = round(float(input("Introduzca el valor para el angulo 3: ")), 2)

    def tamanoMayor(self):
        if self.l1 == self.l2 and self.l1 == self.l3 and self.l2 == self.l3:
            print("No hay valor máximo, ya que todos son iguales")
        else:
            lista = [self.l1, self.l2, self.l3]
            lista.sort(reverse=True)
            print(f"El valor mayor del triangulo es: {lista[0]}")

    def tipoTriangulo(self):
        if self.l1 != self.l2 and self.l1 != self.l3 and self.l2 != self.l3:
            print("El triángulo es escaleno (Todos los lados desiguales)")
        elif self.l1 == self.l2 and self.l1 == self.l3 and self.l2 == self.l3:
            print("El triángulo es equilátero (Todos los lados iguales)")
        else:
            print("El triangulo es isósceles (Dos lados iguales y uno desigual)")


triangulo1 = Triangulo()
triangulo1.tamanoMayor()
triangulo1.tipoTriangulo()