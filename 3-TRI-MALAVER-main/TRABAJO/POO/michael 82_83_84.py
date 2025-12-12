#ejercicio 82
class PersonaNieto:
    def __init__(self, nombre_michael, edad_david):
        self.nombre_michael = nombre_michael
        self.edad_david = edad_david

    def saludar_moreno(self):
        print(f"Hola, soy {self.nombre_michael} y tengo {self.edad_david} aÃ±os")

p1 = PersonaNieto("michael", 20)
p1.saludar_moreno()


#ejercicio 83
class Libromichael:
    def __init__(self, titulo_david):
        self.titulo_david = titulo_david

    def mostrar_nieto(self):
        print(f"El tÃ­tulo del libro es {self.titulo_david}")

libro_moreno = Libromichael("Python FÃ¡cil")
libro_moreno.mostrar_nieto()


#ejercicio 84
class EstudianteDavid:
    def __init__(self, nombre_moreno, nota_michael):
        self.nombre_moreno = nombre_moreno
        self.nota_michael = nota_michael

    def aprobado_nieto(self):
        if self.nota_michael >= 3.0:
            print(f"{self.nombre_moreno} aprobÃ³ con nota {self.nota_michael}")
        else:
            print(f"{self.nombre_moreno} no aprobÃ³, su nota fue {self.nota_michael}")

estu_michael = EstudianteDavid("David", 4.5)
estu_michael.aprobado_nieto()

