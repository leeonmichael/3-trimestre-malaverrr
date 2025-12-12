
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Equipo:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

michael_david_moreno_nieto = Jugador("michael David Moreno Nieto")
mi_equipo = Equipo()
mi_equipo.agregar_jugador(michael_david_moreno_nieto)
for j in mi_equipo.jugadores:
    print(j.nombre)






