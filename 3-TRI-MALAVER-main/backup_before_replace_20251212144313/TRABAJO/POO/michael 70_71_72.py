#ejercicio 70
class Textomichael:
    def contar_palabras(self, texto):
        return len(texto.split())

moreno = Textomichael()
print(moreno.contar_palabras("Hola soy michael Moreno Nieto"))




#ejercicio 71
class NumeroMoreno:
    def convertir(self, numero):
        return str(numero)

david = NumeroMoreno()
print(type(david.convertir(100)))




#ejercicio 72
class Multiplicadormichael:
    def multiplicar_lista(self, lista):
        resultado = 1
        for n in lista:
            resultado *= n
        return resultado

nieto = Multiplicadormichael()
print(nieto.multiplicar_lista([2, 3, 4]))

