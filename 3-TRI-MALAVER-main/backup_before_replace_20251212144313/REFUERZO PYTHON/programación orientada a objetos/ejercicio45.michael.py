

class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Tienda:
    def __init__(self):
        self.inventario = []
    def agregar_producto(self, producto):
        self.inventario.append(producto)

michael_david_moreno_nieto = Producto("Laptop", 5)
mi_tienda = Tienda()
mi_tienda.agregar_producto(michael_david_moreno_nieto)
print([(p.nombre, p.cantidad) for p in mi_tienda.inventario])



class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def acelerar(self, incremento):
        self.velocidad += incremento
    def frenar(self, decremento):
        self.velocidad -= decremento

michael_david_moreno_nieto = Vehiculo("Coche", 60)
michael_david_moreno_nieto.acelerar(20)
michael_david_moreno_nieto.frenar(10)
print(michael_david_moreno_nieto.velocidad)
