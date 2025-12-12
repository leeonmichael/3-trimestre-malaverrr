class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def crear_amigo(self, nombre_amigo):
        return Persona(nombre_amigo)

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
amigo = michael_david_moreno_nieto.crear_amigo("Juan")
print(amigo.nombre)
