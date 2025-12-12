class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        print("Miau")

michael_david_moreno_nieto = Gato()
michael_david_moreno_nieto.sonido()
