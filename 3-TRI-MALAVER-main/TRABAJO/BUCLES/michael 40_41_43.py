#EJERCICIO 40
numero_david = int(input("NÃºmero: "))
es_primo_nieto = True
for michael in range(2, numero_david):
    if numero_david % michael == 0:
        es_primo_nieto = False
        break
print("Primo" if es_primo_nieto else "No primo")



#EJERCICIO 41
numeros_michael = [4, 8, 6, 10, 2]
suma_david = 0
for num_moreno in numeros_michael:
    suma_david += num_moreno
promedio_nieto = suma_david / len(numeros_michael)
print("Promedio:", promedio_nieto)



#EJERCICIO 43
lista_moreno = [-2, 4, -1, 5, 7]
positivos_michael = 0
for valor_david in lista_moreno:
    if valor_david > 0:
        positivos_michael += 1
print("Positivos:", positivos_michael)

