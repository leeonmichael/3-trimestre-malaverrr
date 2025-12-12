

class Nadador:
    def nadar(self):
        print("trotando")

class Corredor:
    def correr(self):
        print("trepando")

class Atleta(Nadador, Corredor):
    pass

michael_david_moreno_nieto = Atleta()
michael_david_moreno_nieto.nadar()
michael_david_moreno_nieto.correr()



