# Class = blueprint
class Person:

    # Constructor = runs when object is created
    def __init__(self, name, age):
        self.name = name
        self.age = age


    # Method = function inside class
    def greet(self):
        print("Hello, ", self.name)



# Object = created from class
p = Person("Alice", 22)
p2 = Person("Rahul", 30)

p.greet()
p2.greet()