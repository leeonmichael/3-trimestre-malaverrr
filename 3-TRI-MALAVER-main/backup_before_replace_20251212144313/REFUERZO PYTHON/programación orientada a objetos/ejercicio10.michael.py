

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

michael_david_moreno_nieto = Curso("software")
michael_david_moreno_nieto.agregar_estudiante("michael David Moreno Nieto")
print(michael_david_moreno_nieto.estudiantes)




