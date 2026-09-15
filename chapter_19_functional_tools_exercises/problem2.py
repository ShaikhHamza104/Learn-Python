"""
📚 Topic: Closure-Based Bank Account State

This script implements encapsulated state management using closures to maintain
a shared private balance.

💡 Key points:
    1️⃣ Enclosing state within outer function scope
    2️⃣ Mutating outer scope state using the `nonlocal` keyword
    3️⃣ Returning multiple function interfaces accessing shared private state
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
