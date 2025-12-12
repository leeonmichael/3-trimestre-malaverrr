# michael moreno
def main():
    print("=== PROGRAMA INTERACTIVO ===")
    nombre = input("Â¿CuÃ¡l es tu nombre? ")
    apellido = input("Â¿CuÃ¡l es tu apellido? ")
    edad = int(input("Â¿CuÃ¡ntos aÃ±os tienes? "))
    altura = float(input("Â¿CuÃ¡l es tu altura en metros? (ej: 1.75) "))
    peso = float(input("Â¿CuÃ¡l es tu peso en kg? "))
    imc = peso / (altura ** 2)
    aÃ±o_actual = 2025
    aÃ±o_nacimiento = aÃ±o_actual - edad

    print("\n" + "="*30)
    print(f"Nombre completo: {nombre} {apellido}")
    print(f"Edad: {edad} aÃ±os")
    print(f"AÃ±o de nacimiento aproximado: {aÃ±o_nacimiento}")
    print(f"Altura: {altura} m, Peso: {peso} kg")
    print(f"IMC: {imc:.2f}")

if __name__ == '__main__':
    main()

