from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("omawae wa mou shindeiru")

michael_david_moreno_nieto = Perro()
michael_david_moreno_nieto.sonido()


