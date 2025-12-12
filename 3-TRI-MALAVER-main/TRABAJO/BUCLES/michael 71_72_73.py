#EJERCICIO 71
frase_david = input("Frase: ")
palabras_michael = frase_david.split()
print("Cantidad de palabras:", len(palabras_michael))



#EJERCICIO 72
notas_moreno = [3.5, 4.0, 2.8, 4.5]
suma_michael = 0
for nota_nieto in notas_moreno:
    suma_michael += nota_nieto
promedio_david = suma_michael / len(notas_moreno)
print("Promedio:", promedio_david)


#EJERCICIO 73
for michael in range(1, 11):
    doble_moreno = michael * 2
    print(doble_moreno)

