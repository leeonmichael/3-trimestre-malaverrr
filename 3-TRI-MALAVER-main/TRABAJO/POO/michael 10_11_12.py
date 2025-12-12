#ejercicio 10
class Alumnomichael:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def cambiar_nota(self, nueva):
        self.nota = nueva

    def mostrar(self):
        print(f"{self.nombre} tiene nota {self.nota}")

david = Alumnomichael("michael", 4.0)
david.cambiar_nota(4.8)
david.mostrar()



#ejercicio 11
class AnimalMoreno:
    def hablar(self):
        print("Soy un animal")

class PerroDavid(AnimalMoreno):
    def hablar(self):
        print("Guau!")

nieto = PerroDavid()
nieto.hablar()



#ejercicio 12
class Amichael:
    def metodo_a(self):
        print("MÃ©todo A")

class BDavid:
    def metodo_b(self):
        print("MÃ©todo B")

class CHijoMoreno(Amichael, BDavid):
    pass

nieto = CHijoMoreno()
nieto.metodo_a()
nieto.metodo_b()

