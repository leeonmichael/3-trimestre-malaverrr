# michael moreno
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

def main():
    palabra = input("Ingresa una palabra: ")
    if es_palindromo(palabra):
        print("La palabra es palÃ­ndroma.")
    else:
        print("La palabra no es palÃ­ndroma.")

if __name__ == '__main__':
    main()

