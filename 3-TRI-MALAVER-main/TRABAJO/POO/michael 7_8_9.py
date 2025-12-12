#ejercicio 7
class ContadorMoreno:
    def contar(self, limite):
        for i in range(1, limite + 1):
            print(i)

nieto = ContadorMoreno()
nieto.contar(5)



#ejercicio 8
class ListaDavid:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def mostrar(self):
        print(self.elementos)

michael = ListaDavid()
michael.agregar("Python")
michael.agregar("POO")
michael.mostrar()



#ejercicio 9
class CuentaMoreno:
    def __init__(self, saldo):
        self.__saldo = saldo

    def mostrar_saldo(self):
        print("Saldo:", self.__saldo)

cuenta_nieto = CuentaMoreno(5000)
cuenta_nieto.mostrar_saldo()

