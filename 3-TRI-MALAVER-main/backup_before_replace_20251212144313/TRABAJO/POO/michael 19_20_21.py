#ejercicio 19}
class TextoMoreno:
    def contar_caracteres(self, texto):
        return len(texto)

t = TextoMoreno()
print("Cantidad:", t.contar_caracteres("michael"))



#ejercicio 20
class Palabramichael:
    def invertir(self, palabra):
        return palabra[::-1]

david = Palabramichael()
print(david.invertir("moreno"))



#ejercicio 21
class Calculadoramichael:
    def doble(self, numero):
        return numero * 2

david = Calculadoramichael()
print(david.doble(10))

