class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

michael_david_moreno_nieto = CuentaBancaria("michael David Moreno Nieto", 1000)
michael_david_moreno_nieto.retirar(200)
print(michael_david_moreno_nieto.saldo)
