
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

michael_david_moreno_nieto = Producto("pc", 1500)
mi_tienda = Tienda()
mi_tienda.agregar_producto(michael_david_moreno_nieto)
for p in mi_tienda.productos:
    print(p.nombre, p.precio)




