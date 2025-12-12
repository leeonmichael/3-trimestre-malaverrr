#ejercicio 49
class Listamichael:
    def unir(self, lista):
        return " ".join(lista)

moreno = Listamichael()
print(moreno.unir(["Hola", "David", "Moreno"]))



#ejercicio 50
class SumaNieto:
    def sumar_hasta(self, n):
        return sum(range(1, n+1))

david = SumaNieto()
print(david.sumar_hasta(10))




#ejercicio 51
class CuentaAtrasmichael:
    def contar(self, inicio):
        for i in range(inicio, 0, -1):
            print(i)

moreno = CuentaAtrasmichael()
moreno.contar(5)

