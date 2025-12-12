#ejercicio 31
class NumeroMoreno:
    def es_par(self, numero):
        return numero % 2 == 0

michael = NumeroMoreno()
print("Â¿Es par?", michael.es_par(6))



#ejercicio 32
class ObjetoDavid:
    total = 0

    def __init__(self):
        ObjetoDavid.total += 1

for _ in range(4):
    ObjetoDavid()

print("Total objetos creados:", ObjetoDavid.total)



#ejercicio 33
class TablaNieto:
    def mostrar_tabla(self, numero):
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero*i}")

michael = TablaNieto()
michael.mostrar_tabla(5)

