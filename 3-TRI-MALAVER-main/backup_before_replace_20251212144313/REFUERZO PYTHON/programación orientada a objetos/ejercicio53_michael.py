class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
    def info(self):
        print(f"{self.nombre} trabaja como {self.cargo}")

michael_david_moreno_nieto = Empleado("michael David Moreno Nieto", "Ingeniero")
michael_david_moreno_nieto.info()
def cuadrados_mayores_que(michael_david_moreno_nieto_lista, michael_david_moreno_nieto_n):
    return [x**2 for x in michael_david_moreno_nieto_lista if x**2 > michael_david_moreno_nieto_n]

print(cuadrados_mayores_que([1,2,3,4,5], 10))



def numeros_pares(michael_david_moreno_nieto_inicio, michael_david_moreno_nieto_fin):
    return [x for x in range(michael_david_moreno_nieto_inicio, michael_david_moreno_nieto_fin+1) if x%2==0]

print(numeros_pares(1,10))
