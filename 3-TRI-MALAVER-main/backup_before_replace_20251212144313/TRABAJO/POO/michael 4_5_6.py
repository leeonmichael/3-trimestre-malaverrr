#EJERCICIO 4
class Cuadradomichael:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

david = Cuadradomichael(4)
print("Ãrea:", david.area())



#EJERCICIO 5
class RectanguloMoreno:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

nieto = RectanguloMoreno(5, 3)
print("PerÃ­metro:", nieto.perimetro())



#EJERCICIO 6
class Calculadoramichael:
    def sumar(self, a, b):
        return a + b

calc_david = Calculadoramichael()
print(calc_david.sumar(5, 7))

