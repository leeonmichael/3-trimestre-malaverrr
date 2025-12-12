

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
    def total(self):
        return sum(p.precio for p in self.productos)
    def total_con_descuento(self, porcentaje):
        return self.total() * (1 - porcentaje / 100)

michael_david_moreno_nieto = Producto("Teclado", 50)
pedido = Pedido()
pedido.agregar_producto(michael_david_moreno_nieto)
print(pedido.total_con_descuento(10))




