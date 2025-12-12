# michael moreno
def main():
    n = int(input("Â¿CuÃ¡ntos nÃºmeros quieres? "))
    lista = [i**2 for i in range(1, n+1)]
    print("Lista de cuadrados:", lista)

if __name__ == '__main__':
    main()

