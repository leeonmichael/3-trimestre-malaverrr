class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Atleta(Nadador, Corredor):
    pass

michael_david_moreno_nieto = Atleta()
michael_david_moreno_nieto.nadar()
michael_david_moreno_nieto.correr()
