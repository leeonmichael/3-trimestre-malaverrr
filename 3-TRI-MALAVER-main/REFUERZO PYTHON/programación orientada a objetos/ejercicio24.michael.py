
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje/100)

michael_david_moreno_nieto = Producto("traje", 50)
michael_david_moreno_nieto.aplicar_descuento(20)
print(michael_david_moreno_nieto.precio)





