class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self, otra_persona):
        print(f"Hola {otra_persona}, soy {self.nombre}")

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
michael_david_moreno_nieto.saludar("Juan")
