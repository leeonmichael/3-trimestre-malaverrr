#ejercicio 25
class TemperaturaNieto:
    def celsius_a_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

david = TemperaturaNieto()
print("Fahrenheit:", david.celsius_a_fahrenheit(30))



#ejercicio 26
class ListaMoreno:
    def suma_lista(self, numeros):
        return sum(numeros)

michael = ListaMoreno()
print(michael.suma_lista([1, 2, 3, 4, 5]))



#ejercicio 27
class Diccionariomichael:
    def __init__(self):
        self.datos = {"nombre": "David", "edad": 25}

    def mostrar(self):
        for clave, valor in self.datos.items():
            print(clave, ":", valor)

moreno = Diccionariomichael()
moreno.mostrar()

