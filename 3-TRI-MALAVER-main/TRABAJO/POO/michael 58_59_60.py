#ejercicio 58
class NumeroDavid:
    def mayor(self, lista):
        return max(lista)

michael = NumeroDavid()
print(michael.mayor([3, 9, 7, 5]))




#ejercicio 59
class DigitosMoreno:
    def sumar_digitos(self, numero):
        return sum(int(d) for d in str(numero))

nieto = DigitosMoreno()
print(nieto.sumar_digitos(1234))




#ejercicio 60
class Listamichael:
    def a_diccionario(self, lista):
        return {i: lista[i] for i in range(len(lista))}

david = Listamichael()
print(david.a_diccionario(["Moreno", "Nieto", "michael"]))

