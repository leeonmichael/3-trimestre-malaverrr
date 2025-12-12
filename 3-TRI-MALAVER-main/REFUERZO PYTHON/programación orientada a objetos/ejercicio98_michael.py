class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def duplicar(self):
        return Persona(self.nombre + " Jr.")

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
nuevo_michael = michael_david_moreno_nieto.duplicar()
print(nuevo_michael.nombre)
