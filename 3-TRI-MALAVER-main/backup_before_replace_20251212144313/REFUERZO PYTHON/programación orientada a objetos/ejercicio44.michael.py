class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []
    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
juan = Persona("pepe")
michael_david_moreno_nieto.agregar_amigo(juan)
print([a.nombre for a in michael_david_moreno_nieto.amigos])
