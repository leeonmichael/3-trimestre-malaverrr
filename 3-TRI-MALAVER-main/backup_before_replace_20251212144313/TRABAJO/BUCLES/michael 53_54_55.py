#EJERCICIO 53
for david in range(3, 31, 3):
    print(david)



#EJERCICIO 54
frase_moreno = input("Frase: ").lower()
letra_michael = input("Letra a contar: ").lower()
contador_nieto = 0
for caracter_david in frase_moreno:
    if caracter_david == letra_michael:
        contador_nieto += 1
print("Aparece:", contador_nieto, "veces")



#EJERCICIO 55
lista_michael = [1, 2, 3, 4, 5, 6]
for moreno in lista_michael:
    if moreno % 2 == 0:
        print(moreno)

