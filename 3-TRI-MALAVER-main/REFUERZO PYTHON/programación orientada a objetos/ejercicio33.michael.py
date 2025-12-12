

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def listar_libros(self):
        return [l.titulo for l in self.libros]

michael_david_moreno_nieto = Libro("Python BÃ¡sico")
mi_biblioteca = Biblioteca()
mi_biblioteca.agregar_libro(michael_david_moreno_nieto)
print(mi_biblioteca.listar_libros())



