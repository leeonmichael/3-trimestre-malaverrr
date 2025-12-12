class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.atributos = {}

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
michael_david_moreno_nieto.atributos["altura"] = 1.75
print(michael_david_moreno_nieto.atributos)
