class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Juego:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

michael_david_moreno_nieto = Jugador("michael David Moreno Nieto")
juego1 = Juego()
juego1.agregar_jugador(michael_david_moreno_nieto)
for j in juego1.jugadores:
    print(j.nombre)
