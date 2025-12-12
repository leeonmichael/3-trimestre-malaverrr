#EJERCICIO 25
for moreno in range(1, 11):
    print(moreno**2)


#EJERCICIO 26
numero_david = int(input("NÃºmero: "))
factorial_nieto = 1
for i in range(1, numero_david + 1):
    factorial_nieto *= i
print("Factorial:", factorial_nieto)


#EJERCICIO 27
a_michael, b_david = 0, 1
for _ in range(10):
    print(a_michael)
    a_michael, b_david = b_david, a_michael + b_david

