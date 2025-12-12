

class Persona:
    def actividad(self):
        print("actuando como persona")

class Profesor(Persona):
    def actividad(self):
        print("pensando en la clase")

michael_david_moreno_nieto = Profesor()
michael_david_moreno_nieto.actividad()



