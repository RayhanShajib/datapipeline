from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, sound:str,  color:str) -> None:
        self.__sound = sound
        self.__color = color

        return None
    
    def makeSound(self) -> None:
        print(self.__sound)

        return None
    
    def makeColor(self) -> None:
        print(self.__color)

        return None
    
class Cat(Animal):
    def __init__(self) -> None:
        super().__init__("meow", "white")
        return None
    
cat1 = Cat()
cat1.makeSound()
cat1.makeColor()