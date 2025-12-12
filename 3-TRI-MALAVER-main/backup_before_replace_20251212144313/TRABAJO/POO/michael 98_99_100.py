#ejercicio 98
class Palindromomichael:
    def __init__(self, palabra_moreno):
        self.palabra_moreno = palabra_moreno.lower()

    def es_palindromo_david(self):
        if self.palabra_moreno == self.palabra_moreno[::-1]:
            print(f"La palabra '{self.palabra_moreno}' es un palÃ­ndromo.")
            return True
        else:
            print(f"La palabra '{self.palabra_moreno}' no es un palÃ­ndromo.")
            return False

texto_nieto = Palindromomichael("Reconocer")
texto_nieto.es_palindromo_david()


#ejercicio 99
class FactorialDavid:
    def __init__(self, numero_michael):
        self.numero_michael = numero_michael

    def calcular_factorial_moreno(self):
        factorial_nieto = 1
        for i_david in range(1, self.numero_michael + 1):
            factorial_nieto *= i_david
        print(f"El factorial de {self.numero_michael} es {factorial_nieto}")
        return factorial_nieto

num_moreno = FactorialDavid(5)
num_moreno.calcular_factorial_moreno()



#ejercicio 100
class TablaMultiplicarmichael:
    def __init__(self, numero_david):
        self.numero_david = numero_david

    def generar_tabla_moreno(self):
        print(f"Tabla de multiplicar del {self.numero_david}:")
        for i_nieto in range(1, 11):
            resultado_michael = self.numero_david * i_nieto
            print(f"{self.numero_david} x {i_nieto} = {resultado_michael}")

tabla_moreno = TablaMultiplicarmichael(7)
tabla_moreno.generar_tabla_moreno()

