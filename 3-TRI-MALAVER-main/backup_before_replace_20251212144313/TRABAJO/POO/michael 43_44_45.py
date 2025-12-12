#ejercicio 43
class TextoDavid:
    def unir(self, t1, t2):
        return t1 + " " + t2

michael = TextoDavid()
print(michael.unir("Hola", "Moreno"))



#ejercicio 44
class CuadradoNieto:
    def generar_cuadrados(self, n):
        return [i**2 for i in range(1, n+1)]

moreno = CuadradoNieto()
print(moreno.generar_cuadrados(5))



#ejercicio 45
class Textomichael:
    def separar_palabras(self, texto):
        return texto.split()

david = Textomichael()
print(david.separar_palabras("michael Moreno Nieto"))

