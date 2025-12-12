class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

michael_david_moreno_nieto = Gerente("michael David Moreno Nieto", 5000, "Ventas")
print(michael_david_moreno_nieto.nombre, michael_david_moreno_nieto.departamento)
