class Direccion:
    def __init__(self, ciudad):
        self.ciudad = ciudad

class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

direccion_kslc = Direccion("BogotÃ¡")
michael_david_moreno_nieto = Persona("michael David Moreno Nieto", direccion_kslc)
print(michael_david_moreno_nieto.direccion.ciudad)
