def greet_decorator(func):
    def wrapper():
        print("Before greeting..")
        func()
        print("After greeting")
    return wrapper


@greet_decorator
def say_hello():
    print("Hello...")


say_hello()