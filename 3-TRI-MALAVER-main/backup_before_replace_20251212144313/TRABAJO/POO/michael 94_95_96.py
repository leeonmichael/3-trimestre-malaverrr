# Ejercicio 74
class InversorTextoMoreno:
    def __init__(self, texto_michael):
        self.texto_michael = texto_michael

    def invertir_david(self):
        texto_invertido_nieto = self.texto_michael[::-1]
        print(f"Texto original: {self.texto_michael}")
        print(f"Texto invertido: {texto_invertido_nieto}")
        return texto_invertido_nieto

texto_moreno = InversorTextoMoreno("michael David")
texto_moreno.invertir_david()



# Ejercicio 75
class NumeroPrimomichael:
    def __init__(self, numero_moreno):
        self.numero_moreno = numero_moreno

    def es_primo_david(self):
        if self.numero_moreno < 2:
            print(f"El nÃºmero {self.numero_moreno} no es primo.")
            return False
        for i_nieto in range(2, int(self.numero_moreno ** 0.5) + 1):
            if self.numero_moreno % i_nieto == 0:
                print(f"El nÃºmero {self.numero_moreno} no es primo.")
                return False
        print(f"El nÃºmero {self.numero_moreno} es primo.")
        return True

num_michael = NumeroPrimomichael(17)
num_michael.es_primo_david()



# Ejercicio 96
class ContadorParesMoreno:
    def __init__(self, lista_michael):
        self.lista_michael = lista_michael

    def contar_pares_david(self):
        contador_nieto = 0
        for numero_moreno in self.lista_michael:
            if numero_moreno % 2 == 0:
                contador_nieto += 1
        print(f"En la lista {self.lista_michael} hay {contador_nieto} nÃºmeros pares.")
        return contador_nieto

numeros_michael = ContadorParesMoreno([1, 2, 3, 4, 5, 6, 8, 9])
numeros_michael.contar_pares_david()

