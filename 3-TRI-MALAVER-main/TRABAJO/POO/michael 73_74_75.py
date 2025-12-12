#ejercicio 73
class ContadorParesDavid:
    def contar(self, lista):
        return sum(1 for n in lista if n % 2 == 0)

michael = ContadorParesDavid()
print(michael.contar([1,2,3,4,5,6]))



#ejercicio 74
class TextoMoreno:
    def filtrar_largas(self, palabras):
        return [p for p in palabras if len(p) > 5]

david = TextoMoreno()
print(david.filtrar_largas(["python", "michael", "sol", "programar"]))



#ejercicio 75
class BuscadorNieto:
    def existe(self, lista, elemento):
        return elemento in lista

michael = BuscadorNieto()
print(michael.existe(["moreno", "david", "michael"], "david"))

