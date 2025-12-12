

class Deportista:
    def entrenar(self):
        print("Entrenando")

class Musico:
    def tocar(self):
        print("Tocando mÃºsica")

class Persona(Deportista, Musico):
    def __init__(self, nombre):
        self.nombre = nombre

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
michael_david_moreno_nieto.entrenar()
michael_david_moreno_nieto.tocar()



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hobbies = []
    def agregar_hobby(self, hobby):
        self.hobbies.append(hobby)

michael_david_moreno_nieto = Persona("michael David Moreno Nieto")
michael_david_moreno_nieto.agregar_hobby("voleibol")
print(michael_david_moreno_nieto.hobbies)
