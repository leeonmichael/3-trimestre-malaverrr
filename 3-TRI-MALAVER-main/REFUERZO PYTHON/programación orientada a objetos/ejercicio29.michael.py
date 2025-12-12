

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def estudiar(self):
        print(f"{self.nombre} estÃ¡ estudiando")

michael_david_moreno_nieto = Estudiante("michael David Moreno Nieto")
michael_david_moreno_nieto.estudiar()



