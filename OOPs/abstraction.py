from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def sound(self):
        return "Meow!"
    
d = Dog()
c = Cat()

print(d.sound())
print(c.sound())