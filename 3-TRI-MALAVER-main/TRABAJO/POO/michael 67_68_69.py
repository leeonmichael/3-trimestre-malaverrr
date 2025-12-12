#ejercicio 67
class Imparesmichael:
    def sumar_impares(self, lista):
        return sum([x for x in lista if x % 2 != 0])

david = Imparesmichael()
print(david.sumar_impares([1,2,3,4,5]))




#ejercicio 68
import random

class AleatorioMoreno:
    def generar(self, inicio, fin):
        return random.randint(inicio, fin)

michael = AleatorioMoreno()
print(michael.generar(1, 100))




#ejercicio 69
class ListaDavid:
    def eliminar_duplicados(self, lista):
        return list(set(lista))

nieto = ListaDavid()
print(nieto.eliminar_duplicados([1,2,2,3,3,4]))

