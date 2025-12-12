

class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    def promedio(self):
        return sum(self.notas) / len(self.notas)

michael_david_moreno_nieto = Estudiante("michael David Moreno Nieto", [80, 90, 70])
print(michael_david_moreno_nieto.promedio())



