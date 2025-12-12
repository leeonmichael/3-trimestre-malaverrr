class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __len__(self):
        return len(self.nombre)

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
print(len(michael_david_moreno_nieto))
