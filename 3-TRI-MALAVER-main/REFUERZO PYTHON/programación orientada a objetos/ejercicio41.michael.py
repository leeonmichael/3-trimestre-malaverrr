
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def obtener_velocidad(self):
        return self.velocidad

michael_david_moreno_nieto = Vehiculo("Moto", 80)
print(michael_david_moreno_nieto.obtener_velocidad())



