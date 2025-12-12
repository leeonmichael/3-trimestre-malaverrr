
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __str__(self):
        return f"{self.tipo} a {self.velocidad} km/h"

michael_david_moreno_nieto = Vehiculo("Coche", 100)
print(michael_david_moreno_nieto)




