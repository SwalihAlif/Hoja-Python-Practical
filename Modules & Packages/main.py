import utility
from my_package import calculator, greeter

print(utility.greet("Alice"))
print(utility.add(10, 20))


print(greeter.say_hello("Rahul"))

added = calculator.add(100, 200)
print("Added: ", added)

sub = calculator.subtract(added, 5)

print("Sub: ", sub)