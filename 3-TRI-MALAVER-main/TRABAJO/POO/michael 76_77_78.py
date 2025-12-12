#ejercicio 76
class Listamichael:
    def indice(self, lista, valor):
        return lista.index(valor) if valor in lista else -1

moreno = Listamichael()
print(moreno.indice(["a", "b", "c"], "b"))



#ejercicio 77
class ListaDavid:
    def reemplazar(self, lista, viejo, nuevo):
        return [nuevo if x == viejo else x for x in lista]

nieto = ListaDavid()
print(nieto.reemplazar([1,2,3,2,4], 2, 99))



#ejercicio 78
class CuadradoMoreno:
    def sumar_cuadrados(self, lista):
        return sum(x**2 for x in lista)

michael = CuadradoMoreno()
print(michael.sumar_cuadrados([1,2,3,4]))

