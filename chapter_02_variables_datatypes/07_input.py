"""
📚 Topic: Capturing User Input with `input()`

This script demonstrates reading terminal user input using `input()`,
inspecting the captured strings, and understanding default string typing.

💡 Key points:
    1️⃣ Prompting the user for console input using `input("...")`
    2️⃣ Storing user responses in variables for display and processing
    3️⃣ Understanding why `input()` always returns a string (`str`)

🧠 Beginner tip:
    Because `input()` always returns text, any numbers entered must be
    explicitly converted using `int()` or `float()` before doing arithmetic.
"""

# 🔤 Take the first value from the user
a = input("Enter the first number: ")

# 🔤 Take the second value from the user
b = input("Enter the second number: ")

# 🖨️ Display the values entered by the user
print("First number is:", a)
print("Second number is:", b)

# 🔍 Check the data type of both inputs
# `input()` returns strings by default
print(type(a), type(b))

# ➕ Convert both strings into integers and add them
print(int(a) + int(b))
