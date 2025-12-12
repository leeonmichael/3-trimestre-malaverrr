class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asistencias = 0
    def registrar_asistencia(self):
        self.asistencias += 1

michael_david_moreno_nieto = Alumno("michael David Moreno Nieto")
michael_david_moreno_nieto.registrar_asistencia()
print(michael_david_moreno_nieto.asistencias)
