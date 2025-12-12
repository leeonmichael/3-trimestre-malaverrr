

class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

michael_david_moreno_nieto1 = Persona("michael David Moreno Nieto")
michael_david_moreno_nieto2 = Persona("michael Nieto")
print(Persona.contador)





