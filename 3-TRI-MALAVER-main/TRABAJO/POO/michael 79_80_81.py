#ejercicio 79
class TextoNieto:
    def contar_mayusculas(self, texto):
        return sum(1 for l in texto if l.isupper())

david = TextoNieto()
print(david.contar_mayusculas("michael David MORENO"))



#ejercicio 80
class Personamichael:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} aÃ±os.")

class EstudianteDavid(Personamichael):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def mostrar(self):
        print(f"{self.nombre} ({self.edad} aÃ±os) estudia {self.curso}")

moreno = EstudianteDavid("michael David Moreno Nieto", 22, "ProgramaciÃ³n")
moreno.saludar()
moreno.mostrar()



#ejercicio 81
# Ejercicio 61 - Creado por michael David Moreno Nieto
class Vehiculomichael:
    def __init__(self, marca_michael, modelo_david):
        self.marca_michael = marca_michael
        self.modelo_david = modelo_david

auto_moreno = Vehiculomichael("Yamaha", "2025")
print("Marca:", auto_moreno.marca_michael)
print("Modelo:", auto_moreno.modelo_david)

