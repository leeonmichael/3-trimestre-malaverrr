#ejercicio 91
class Notasmichael:
    def __init__(self, nota1_david, nota2_moreno, nota3_nieto):
        self.nota1_david = nota1_david
        self.nota2_moreno = nota2_moreno
        self.nota3_nieto = nota3_nieto

    def calcular_promedio_michael(self):
        promedio = (self.nota1_david + self.nota2_moreno + self.nota3_nieto) / 3
        print(f"El promedio de michael David Moreno Nieto es: {promedio:.2f}")
        return promedio

notas_alumno = Notasmichael(4.0, 3.5, 4.5)
notas_alumno.calcular_promedio_michael()


#ejercicio 92
class TemperaturaDavid:
    def __init__(self, celsius_michael):
        self.celsius_michael = celsius_michael

    def convertir_a_fahrenheit_moreno(self):
        fahrenheit_nieto = (self.celsius_michael * 9/5) + 32
        print(f"{self.celsius_michael}Â°C equivalen a {fahrenheit_nieto}Â°F")
        return fahrenheit_nieto

temp_michael = TemperaturaDavid(25)
temp_michael.convertir_a_fahrenheit_moreno()



#ejercicio 93
class ContadorVocalesmichael:
    def __init__(self, palabra_david):
        self.palabra_david = palabra_david.lower()

    def contar_vocales_moreno(self):
        contador_nieto = 0
        for letra_michael in self.palabra_david:
            if letra_michael in "aeiou":
                contador_nieto += 1
        print(f"La palabra '{self.palabra_david}' tiene {contador_nieto} vocales.")
        return contador_nieto

palabra_michael = ContadorVocalesmichael("Programacion")
palabra_michael.contar_vocales_moreno()

