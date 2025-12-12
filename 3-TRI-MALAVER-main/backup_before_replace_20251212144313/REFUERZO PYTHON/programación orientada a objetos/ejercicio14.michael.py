

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

michael_david_moreno_nieto = Estudiante("michael David Moreno Nieto")
matematicas = Curso()
matematicas.agregar_estudiante(michael_david_moreno_nieto)
print([e.nombre for e in matematicas.estudiantes])


