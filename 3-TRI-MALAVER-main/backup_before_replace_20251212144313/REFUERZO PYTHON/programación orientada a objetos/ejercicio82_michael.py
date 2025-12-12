class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anos(self):
        self.edad += 1

michael_david_moreno_nieto = Persona("michael David Moreno Nieto", 25)
michael_david_moreno_nieto.cumplir_anos()
print(michael_david_moreno_nieto.edad)
