#EJERCICIO 19
# Autor: michael David Moreno Nieto
lista = [3, -1, 5, -6, 2]
negativos = 0
for num in lista:
    if num < 0:
        negativos += 1
print(negativos)



#EJERCICIO 20
# Autor: michael David Moreno Nieto
lista = [3, 5, 7, 9]
prom = sum(lista) / len(lista)
print(prom)



#EJERCICIO 21

numeros_michael = [int(input("NÃºmero: ")) for _ in range(5)]
mayor_david = max(numeros_michael)
print("El mayor es:", mayor_david)

