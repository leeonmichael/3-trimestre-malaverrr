class Poligono:
    def __init__(self, lados):
        self.lados = lados

class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado
    def area(self):
        return self.lado ** 2

michael_david_moreno_nieto = Cuadrado(5)
print(michael_david_moreno_nieto.area())





