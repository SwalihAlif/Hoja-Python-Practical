print("------------ATM SIMULATOR---------")

balance = 5000

#function to show menu
def show_menu():
    print("\n--------------------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


# function to check balance
def check_balance():
    print("Current Balance: ", balance)


# function to deposit
def deposit():
    global balance

    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Rs.", amount, "is deposited.")
        print("Current Balance: ", balance)
    else:
        print("Invalid Amount..")


#function to withdraw
def withdraw():
    global balance

    amount = float(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Please collect your cash, ", amount)
        print("Current Balance: ", balance)
    else:
        print("Insufficient Balance!")

# Main Program
while True:
    show_menu()

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        check_balance()

    elif choice == 2:
        deposit()

    elif choice == 3:
        withdraw()

    elif choice == 4:
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid Choice! Please Try Again.")




