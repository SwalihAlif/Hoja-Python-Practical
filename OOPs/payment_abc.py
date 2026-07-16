from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Card(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Card")

p1 = UPI()
c1 = Card()

p1.pay(500)
c1.pay(1000)