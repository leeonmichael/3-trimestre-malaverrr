#ejercicio 34
class ListaMoreno:
    def invertir_lista(self, lista):
        return lista[::-1]

david = ListaMoreno()
print(david.invertir_lista([1, 2, 3, 4]))



#ejercicio 35
class SumaParesmichael:
    def sumar_pares(self, lista):
        return sum([x for x in lista if x % 2 == 0])

moreno = SumaParesmichael()
print(moreno.sumar_pares([1, 2, 3, 4, 5, 6]))



#ejercicio 36
class TextoDavid:
    def convertir(self, texto):
        return texto.upper()

nieto = TextoDavid()
print(nieto.convertir("michael moreno"))

