
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * porcentaje / 100

michael_david_moreno_nieto = Empleado("michael David Moreno Nieto", 3000)
michael_david_moreno_nieto.aumentar_salario(10)
print(michael_david_moreno_nieto.salario)
