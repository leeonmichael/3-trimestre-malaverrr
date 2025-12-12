class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def filtrar_por_autor(self, autor):
        return [l.titulo for l in self.libros if l.autor == autor]

michael_david_moreno_nieto = Libro("Python Avanzado", "michael David Moreno Nieto")
biblioteca = Biblioteca()
biblioteca.agregar_libro(michael_david_moreno_nieto)
print(biblioteca.filtrar_por_autor("michael David Moreno Nieto"))
