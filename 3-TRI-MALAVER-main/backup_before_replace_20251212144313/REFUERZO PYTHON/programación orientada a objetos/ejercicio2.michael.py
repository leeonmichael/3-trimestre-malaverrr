

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return f"Persona: {self.nombre}"

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
print(michael_david_moreno_nieto)




