"""
📚 Topic: Problem2

This script demonstrates problem2 using closures, nonlocal and
exception handling.

💡 Key points:
    1️⃣ the basic syntax for problem2
    2️⃣ how nonlocal fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem2 affects the result.
"""


# 2. Write a closure-based bank_account function that returns a
# deposit() and withdraw() function, both sharing the same private
# balance variable. Raise an error if withdrawing more than available.
def bank_account(starting_balance=0):
    balance = starting_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        print(f"Deposited {amount}. New balance: {balance}")

    def withdraw(amount):
        nonlocal balance
        try:
            if amount > balance:
                raise ValueError("Insufficient balance")
            balance -= amount
            print(f"Withdrew {amount}. New balance: {balance}")
        except ValueError as e:
            print(e)

    return deposit, withdraw


deposit, withdraw = bank_account(100)

deposit(50)
withdraw(30)
withdraw(1000)
