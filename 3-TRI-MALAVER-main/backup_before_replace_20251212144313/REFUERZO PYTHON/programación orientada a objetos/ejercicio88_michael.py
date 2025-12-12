class Animal:
    def sonido(self):
        print("Hace un sonido")

class Perro(Animal):
    def sonido(self):
        print("Guau!")

michael_david_moreno_nieto = Perro()
michael_david_moreno_nieto.sonido()

