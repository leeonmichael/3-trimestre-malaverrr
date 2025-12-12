#ejercicio 22
class PersonaMoreno:
    def __init__(self):
        self.nombre = "michael"
        self.edad = 20

    def mostrar(self):
        print(f"{self.nombre} tiene {self.edad} aÃ±os")

nieto = PersonaMoreno()
nieto.mostrar()



#ejercicio 23
class ListaNombresDavid:
    def __init__(self):
        self.nombres = []

    def agregar_nombre(self, nombre):
        self.nombres.append(nombre)

    def mostrar_nombres(self):
        print("Lista de nombres:", self.nombres)

michael = ListaNombresDavid()
michael.agregar_nombre("Moreno")
michael.agregar_nombre("Nieto")
michael.mostrar_nombres()



#ejercicio 24
class Notamichael:
    def evaluar(self, nota):
        if nota >= 3:
            print("Aprobado, michael!")
        else:
            print("Reprobado, David!")

moreno = Notamichael()
moreno.evaluar(4)

