try:
    num = int(input("Enter a number"))
    result = 10 / num
    print(result)
except ValueError:
    print("Enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Calculation Successfull.")
finally:
    print("Program Ended. Thank You...")