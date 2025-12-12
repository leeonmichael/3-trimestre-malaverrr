

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
michael_david_moreno_nieto.nombre = "michael Nieto"
print(michael_david_moreno_nieto.nombre)


