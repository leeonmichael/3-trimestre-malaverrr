class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def interes(self, porcentaje):
        self.saldo += self.saldo * porcentaje / 100

michael_david_moreno_nieto = Cuenta("michael David Moreno Nieto", 1000)
michael_david_moreno_nieto.interes(5)
print(michael_david_moreno_nieto.saldo)
