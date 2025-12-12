 

class Banco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    def mostrar_saldo(self):
        print(self.__saldo)

michael_david_moreno_nieto = Banco("michael David Moreno Nieto", 1000)
michael_david_moreno_nieto.mostrar_saldo()





