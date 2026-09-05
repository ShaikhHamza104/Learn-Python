"""
📚 Topic: Input

This script demonstrates input using user input.

💡 Key points:
    1️⃣ the basic syntax for input
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    input affects the result.
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
