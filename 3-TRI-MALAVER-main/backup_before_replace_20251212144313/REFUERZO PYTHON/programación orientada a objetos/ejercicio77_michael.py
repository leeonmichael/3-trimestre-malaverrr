class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def acelerar(self, aumento):
        self.velocidad += aumento

michael_david_moreno_nieto = Vehiculo("Coche", 50)
michael_david_moreno_nieto.acelerar(20)
print(michael_david_moreno_nieto.velocidad)
