#ejercicio 46
class ContadorLetrasMoreno:
    def contar(self, texto):
        return len(texto.replace(" ", ""))

nieto = ContadorLetrasMoreno()
print(nieto.contar("David michael"))



#ejercicio 47
class Triangulomichael:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

david = Triangulomichael(6, 3)
print("Ãrea:", david.area())



#ejercicio 48
class NombresMoreno:
    def __init__(self):
        self.nombres = set()

    def agregar(self, nombre):
        self.nombres.add(nombre)

    def mostrar(self):
        print(self.nombres)

michael = NombresMoreno()
michael.agregar("David")
michael.agregar("David")
michael.agregar("Nieto")
michael.mostrar()

