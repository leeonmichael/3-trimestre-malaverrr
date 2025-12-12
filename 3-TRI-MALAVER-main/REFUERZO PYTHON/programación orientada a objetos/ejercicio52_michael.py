class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def es_mas_rapido_que(self, otro):
        return self.velocidad > otro.velocidad

v1 = Vehiculo("Moto", 120)
v2 = Vehiculo("Coche", 100)
michael_david_moreno_nieto = v1.es_mas_rapido_que(v2)
print(michael_david_moreno_nieto)
