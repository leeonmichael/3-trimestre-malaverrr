
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self):
        self.estudiantes = []
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

michael_david_moreno_nieto = Estudiante("michael David Moreno Nieto")
curso = Curso()
curso.agregar_estudiante(michael_david_moreno_nieto)
print([e.nombre for e in curso.estudiantes])



class Persona:
    def actividad(self):
        print("Realizando actividad")

class Estudiante(Persona):
    def actividad(self):
        print("Estudiando")

michael_david_moreno_nieto = Estudiante()
michael_david_moreno_nieto.actividad()
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anos(self):
        self.edad += 1

michael_david_moreno_nieto = Persona("michael David Moreno Nieto", 25)
michael_david_moreno_nieto.cumplir_anos()
print(michael_david_moreno_nieto.edad)




