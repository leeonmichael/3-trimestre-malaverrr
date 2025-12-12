#ejercicio 88
class CocheDavid:
    def __init__(self, color_michael):
        self.color_michael = color_michael

    def pintar_moreno(self, nuevo_color):
        print(f"El coche cambia de color {self.color_michael} a {nuevo_color}")
        self.color_michael = nuevo_color

auto_michael = CocheDavid("Rojo")
auto_michael.pintar_moreno("Negro")
print(f"Color final del coche: {auto_michael.color_michael}")



#ejercicio 89
class Rectangulomichael:
    def __init__(self, ancho_david, alto_moreno):
        self.ancho_david = ancho_david
        self.alto_moreno = alto_moreno

    def calcular_area_nieto(self):
        area = self.ancho_david * self.alto_moreno
        print(f"El Ã¡rea del rectÃ¡ngulo es: {area}")
        return area

rect_michael = Rectangulomichael(10, 5)
rect_michael.calcular_area_nieto()


#ejercicio 90
class EstudianteMoreno:
    def __init__(self, nombre_michael, edad_david):
        self.nombre_michael = nombre_michael
        self.edad_david = edad_david

    def mostrar_informacion_nieto(self):
        print(f"Nombre del estudiante: {self.nombre_michael}, Edad: {self.edad_david}")

alumno_david = EstudianteMoreno("michael Moreno", 22)
alumno_david.mostrar_informacion_nieto()





