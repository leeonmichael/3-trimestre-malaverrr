#EJERCICIO 10
# Autor: michael David Moreno Nieto
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")


#EJERCICIO 11
# Autor: michael David Moreno Nieto
for n in range(1, 11):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
    print()


#EJERCICIO 12
# Autor: michael David Moreno Nieto
cont = 0
for i in range(1, 51):
    if i % 3 == 0:
        cont += 1
print(cont)

