

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"{self.nombre} cuesta {self.precio} USD"

michael_david_moreno_nieto = Producto("Mouse", 25)
print(michael_david_moreno_nieto)




