

class Auto:
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False
    def encender(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False

michael_david_moreno_nieto = Auto("Toyota")
michael_david_moreno_nieto.encender()
print(michael_david_moreno_nieto.encendido)





