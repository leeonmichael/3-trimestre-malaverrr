#EJERCICIO 31
palabra_david = input("Palabra: ").lower()
consonantes_moreno = 0
for letra_michael in palabra_david:
    if letra_michael.isalpha() and letra_michael not in "aeiou":
        consonantes_moreno += 1
print("Consonantes:", consonantes_moreno)



#EJERCICIO 32
for michael in range(1, 101):
    if michael % 3 == 0:
        print("Fizz")
    else:
        print(michael)



#EJERCICIO 33
for moreno in range(1, 101):
    if moreno % 5 == 0:
        print("Buzz")
    else:
        print(moreno)

