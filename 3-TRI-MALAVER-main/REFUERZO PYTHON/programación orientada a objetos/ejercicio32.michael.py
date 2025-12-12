

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

michael_david_moreno_nieto = Estudiante("michael David Moreno Nieto", "IngenierÃ­a")
print(michael_david_moreno_nieto.nombre, michael_david_moreno_nieto.carrera)



