

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.set_edad(edad)

    def set_edad(self, edad):
        if edad < 0:
            self.edad = 0
        else:
            self.edad = edad

michael_david_moreno_nieto = Persona("michael David Moreno Nieto", -5)
print(michael_david_moreno_nieto.edad)
