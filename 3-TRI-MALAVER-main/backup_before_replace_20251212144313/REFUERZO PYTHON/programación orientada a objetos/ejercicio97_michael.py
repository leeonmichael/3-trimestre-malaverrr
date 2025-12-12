class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

personas = []
personas.append(Persona("michael David Moreno Nieto"))
personas.append(Persona("Juan"))
for p in personas:
    print(p.nombre)
