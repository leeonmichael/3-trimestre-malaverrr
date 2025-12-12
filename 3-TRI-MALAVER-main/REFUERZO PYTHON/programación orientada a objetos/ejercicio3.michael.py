
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre, salario):
        super().__init__(nombre)
        self.salario = salario

michael_david_moreno_nieto = Empleado("michael David Moreno Nieto", 3000)
print(michael_david_moreno_nieto.nombre, michael_david_moreno_nieto.salario)
 


