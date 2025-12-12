#EJERCICIO 37
numeros_david = [3, 4, 7, 8, 10]
for michael in numeros_david:
    if michael % 2 == 0:
        print(michael)



#EJERCICIO 38
numeros_moreno = [3, 4, 7, 8, 10]
for david in numeros_moreno:
    if david % 2 != 0:
        print(david)



#EJERCICIO 39
numero_michael = int(input("NÃºmero: "))
for moreno in range(1, numero_michael + 1):
    if numero_michael % moreno == 0:
        print(moreno)

