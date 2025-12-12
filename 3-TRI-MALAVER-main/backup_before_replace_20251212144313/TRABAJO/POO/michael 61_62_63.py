#ejercicio 61
class Matrizmichael:
    def sumar_elementos(self, matriz):
        total = 0
        for fila in matriz:
            total += sum(fila)
        return total

david = Matrizmichael()
print(david.sumar_elementos([[1,2,3],[4,5,6]]))



#ejercicio 62
class PromedioMoreno:
    def calcular(self, numeros):
        return sum(numeros) / len(numeros)

michael = PromedioMoreno()
print("Promedio:", michael.calcular([2, 4, 6, 8]))



#ejercicio 63
class NumeroNieto:
    def menor(self, lista):
        return min(lista)

david = NumeroNieto()
print(david.menor([10, 2, 5, 8]))

