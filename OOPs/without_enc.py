class BankAccount:
    def __init__(self, balance):
        self.__balance = balance



acc = BankAccount(1000)
print(acc.__balance)
acc.__balance -= 500
print(acc.__balance)

