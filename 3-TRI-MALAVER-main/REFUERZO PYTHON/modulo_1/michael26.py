# michael moreno
def clasificar_edad(edad):
    if edad < 0:
        return "Edad invÃ¡lida"
    if edad <= 12:
        return "NiÃ±o"
    elif edad <= 17:
        return "Adolescente"
    elif edad <= 64:
        return "Adulto"
    else:
        return "Adulto mayor"

def main():
    edad = int(input("Ingresa la edad: "))
    print(clasificar_edad(edad))

if __name__ == '__main__':
    main()

