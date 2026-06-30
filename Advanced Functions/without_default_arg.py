def greet(name=None):
    if name is None:
        name = "Guest"
    print("Hello ", name)

greet()
greet("Alice")