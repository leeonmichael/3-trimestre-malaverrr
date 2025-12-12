class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, cantidad):
        self.saldo += cantidad

michael_david_moreno_nieto = Cuenta("michael David Moreno Nieto", 1000)
michael_david_moreno_nieto.depositar(500)
print(michael_david_moreno_nieto.saldo)
