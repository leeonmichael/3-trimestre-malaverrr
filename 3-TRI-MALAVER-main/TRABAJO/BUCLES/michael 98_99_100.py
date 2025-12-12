#ejercicio 98
palabra_michael = input("Palabra: ").lower()
contador_moreno = 0
for letra_david in palabra_michael:
    if letra_david == "a":
        contador_moreno += 1
print("Letras 'a':", contador_moreno)



#ejercicio 99
for nieto in range(2, 13, 2):
    cuadrado_michael = nieto ** 2
    print(cuadrado_michael)




#ejercicio 100
for david in range(3):
    for moreno in range(1, 6):
        print(moreno, end=" ")
    print()

