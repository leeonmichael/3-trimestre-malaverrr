class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos = {}

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
michael_david_moreno_nieto.datos["edad"] = 25
print(michael_david_moreno_nieto.datos)
