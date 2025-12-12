 

class Secreto:
    def __init__(self, mensaje):
        self.__mensaje = mensaje
    def revelar(self):
        print(self.__mensaje)

michael_david_moreno_nieto = Secreto("michael David Moreno Nieto")
michael_david_moreno_nieto.revelar()


