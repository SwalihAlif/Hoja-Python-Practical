class Shape:
    def area(self):
        return 0
    
class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5
    
class Rectangle(Shape):
    def area(self):
        return 10 * 5
    
#polymorphism
shapes = [Circle(), Rectangle()]

for s in shapes:
    print(s.area())