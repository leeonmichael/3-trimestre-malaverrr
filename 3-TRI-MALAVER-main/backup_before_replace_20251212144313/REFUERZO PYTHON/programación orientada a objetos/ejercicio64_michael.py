class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __repr__(self):
        return f"Vehiculo('{self.tipo}', {self.velocidad})"

michael_david_moreno_nieto = Vehiculo("Bicicleta", 20)
print(repr(michael_david_moreno_nieto))
