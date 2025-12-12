class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrar_materias(self, materias):
        for m in materias:
            print(f"{self.nombre} estudia {m}")

michael_david_moreno_nieto = Alumno("michael David Moreno Nieto")
michael_david_moreno_nieto.mostrar_materias(["MatemÃ¡ticas", "FÃ­sica"])
