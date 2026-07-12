class Animal:
    def eat(self):
        print("Eating...")


class Dog(Animal):
    def bark(self):
        print("Barking...")



a = Dog()
a.eat()
a.bark()