def outer():
    def inner():
        print("Inner function called.")
    print("Outer function started.")
    inner()



outer()