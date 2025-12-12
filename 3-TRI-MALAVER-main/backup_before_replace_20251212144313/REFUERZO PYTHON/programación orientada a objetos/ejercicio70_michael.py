class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    def mostrar_nombre(self):
        print(self.__nombre)

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
michael_david_moreno_nieto.mostrar_nombre()
