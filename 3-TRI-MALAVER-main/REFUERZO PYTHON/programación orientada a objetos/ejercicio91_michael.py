class Luz:
    def __init__(self):
        self.encendida = False
    def cambiar_estado(self):
        self.encendida = not self.encendida

michael_david_moreno_nieto = Luz()
michael_david_moreno_nieto.cambiar_estado()
print(michael_david_moreno_nieto.encendida)
