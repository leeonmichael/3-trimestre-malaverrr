

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sumar(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

p1 = Punto(2, 3)
p2 = Punto(4, 5)
michael_david_moreno_nieto = p1.sumar(p2)
print(michael_david_moreno_nieto.x, michael_david_moreno_nieto.y)



class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self):
        self.productos = []
    def agregar(self, producto):
        self.productos.append(producto)
    def total(self):
        return sum(p.precio for p in self.productos)

michael_david_moreno_nieto = Producto("Teclado", 30)
pedido1 = Pedido()
pedido1.agregar(michael_david_moreno_nieto)
print(pedido1.total())
