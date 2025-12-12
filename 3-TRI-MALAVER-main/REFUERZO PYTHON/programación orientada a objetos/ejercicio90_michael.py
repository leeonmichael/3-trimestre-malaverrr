class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def crear_hijo(self):
        return Persona(self.nombre + " Jr.")

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
hijo = michael_david_moreno_nieto.crear_hijo()
print(hijo.nombre)
