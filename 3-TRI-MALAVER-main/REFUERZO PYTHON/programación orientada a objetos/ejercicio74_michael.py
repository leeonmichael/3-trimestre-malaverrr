class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

michael_david_moreno_nieto = Profesor("michael David Moreno Nieto")
michael_david_moreno_nieto.agregar_materia("MatemÃ¡ticas")
print(michael_david_moreno_nieto.materias)
