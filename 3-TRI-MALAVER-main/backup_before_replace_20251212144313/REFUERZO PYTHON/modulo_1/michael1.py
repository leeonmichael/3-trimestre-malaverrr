# michael moreno
class EdadInvalidaError(Exception):
    pass

def validar_edad(edad):
    if edad < 0 or edad > 150:
        raise EdadInvalidaError(f'Edad {edad} no es vÃ¡lida')
    return edad

def main():
    try:
        validar_edad(-5)
    except EdadInvalidaError as e:
        print('Error de validaciÃ³n:', e)
    else:
        print('Edad vÃ¡lida')

if __name__ == '__main__':
    main()

