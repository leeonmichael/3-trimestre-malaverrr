class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hobbies = []
    def agregar_hobby(self, hobby):
        self.hobbies.append(hobby)

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
michael_david_moreno_nieto.agregar_hobby("matar zombies")
print(michael_david_moreno_nieto.hobbies)
