#ejercicio 16
class Contadormichael:
    total = 0

    @classmethod
    def aumentar(cls):
        cls.total += 1

Contadormichael.aumentar()
Contadormichael.aumentar()
print("Total:", Contadormichael.total)



#ejercicio 17
class SaludoDavid:
    def mensaje(self):
        return "Hola, michael David Moreno Nieto!"

s = SaludoDavid()
print(s.mensaje())



#ejercicio 18
class PersonaNieto:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Persona: {self.nombre}"

p = PersonaNieto("michael")
print(p)

