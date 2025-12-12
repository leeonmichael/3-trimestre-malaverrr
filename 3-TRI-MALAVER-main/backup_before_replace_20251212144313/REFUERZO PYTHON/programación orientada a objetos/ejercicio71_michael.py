class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Atleta(Nadador, Corredor):
    def __init__(self, nombre):
        self.nombre = nombre

michael_david_moreno_nieto = Atleta("michael David Moreno Nieto")
michael_david_moreno_nieto.nadar()
michael_david_moreno_nieto.correr()
