#EJERCICIO 28
numero_moreno = input("NÃºmero: ")
suma_nieto = 0
for digito_michael in numero_moreno:
    suma_nieto += int(digito_michael)
print("Suma de dÃ­gitos:", suma_nieto)



#EJERCICIO 29
numero_david = input("NÃºmero: ")
invertido_michael = numero_david[::-1]
print("Invertido:", invertido_michael)


#EJERCICIO 30
palabra_moreno = input("Palabra: ").lower()
vocales_nieto = 0
for letra_michael in palabra_moreno:
    if letra_michael in "aeiou":
        vocales_nieto += 1
print("Cantidad de vocales:", vocales_nieto)

