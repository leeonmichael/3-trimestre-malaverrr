
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
    @property
    def nombre(self):
        return self._nombre

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
print(michael_david_moreno_nieto.nombre)




