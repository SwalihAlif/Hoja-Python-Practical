import tkinter as tk
from tkinter import messagebox

# Initial Balance
balance = 5000


# ---------------- Functions ---------------- #

def check_balance():
    messagebox.showinfo("Balance", f"Current Balance: ₹{balance}")


def deposit():
    global balance

    amount = entry.get()

    if amount == "":
        messagebox.showwarning("Warning", "Enter an amount.")
        return

    amount = int(amount)

    if amount <= 0:
        messagebox.showerror("Error", "Invalid amount.")
        return

    balance += amount
    messagebox.showinfo("Success", f"₹{amount} Deposited Successfully.")
    entry.delete(0, tk.END)


def withdraw():
    global balance

    amount = entry.get()

    if amount == "":
        messagebox.showwarning("Warning", "Enter an amount.")
        return

    amount = int(amount)

    if amount <= 0:
        messagebox.showerror("Error", "Invalid amount.")
        return

    if amount > balance:
        messagebox.showerror("Error", "Insufficient Balance.")
        return

    balance -= amount
    messagebox.showinfo("Success", f"₹{amount} Withdrawn Successfully.")
    entry.delete(0, tk.END)


# ---------------- GUI ---------------- #

window = tk.Tk()
window.title("ATM Simulator")
window.geometry("350x300")
window.resizable(False, False)

title = tk.Label(
    window,
    text="ATM Simulator",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

label = tk.Label(
    window,
    text="Enter Amount"
)
label.pack()

entry = tk.Entry(
    window,
    font=("Arial", 14)
)
entry.pack(pady=10)

btn1 = tk.Button(
    window,
    text="Check Balance",
    width=20,
    command=check_balance
)
btn1.pack(pady=5)

btn2 = tk.Button(
    window,
    text="Deposit",
    width=20,
    command=deposit
)
btn2.pack(pady=5)

btn3 = tk.Button(
    window,
    text="Withdraw",
    width=20,
    command=withdraw
)
btn3.pack(pady=5)

btn4 = tk.Button(
    window,
    text="Exit",
    width=20,
    command=window.destroy
)
btn4.pack(pady=15)

window.mainloop()