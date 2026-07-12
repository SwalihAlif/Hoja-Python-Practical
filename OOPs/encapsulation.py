class Demo:
    def __init__(self):
        self.public_var = "I am PUBLIC"
        self._protected_var = "I am PROTECTED"
        self.__private_var = "I am PRIVATE"

    def show(self):
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)

    def get_private(self):
        return self.__private_var


obj = Demo()
print(obj.public_var)
print(obj._protected_var)
print(obj.get_private())