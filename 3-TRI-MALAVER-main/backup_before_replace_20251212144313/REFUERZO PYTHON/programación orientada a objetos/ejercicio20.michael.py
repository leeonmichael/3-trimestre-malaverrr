

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def calcular_bono(self):
        return self.salario * 0.1

michael_david_moreno_nieto = Empleado("michael David Moreno Nieto", 3000)
print(michael_david_moreno_nieto.calcular_bono())




