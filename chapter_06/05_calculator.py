"""
📚 Topic: Calculator

This script demonstrates calculator using conditions and user input.

💡 Key points:
    1️⃣ the basic syntax for calculator
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    calculator affects the result.
"""


# 🧮 Display the calculator title
print("""
This is a calculator which performs +, -, * and /
""")

# 🔢 Take the first number
num1 = int(input("Enter 1 number: "))

# ➕➖✖️➗ Ask the user for an operator
operator = input("Enter operator: ")

# 🔢 Take the second number
num2 = int(input("Enter 2 number: "))

# ➕ Addition
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

# ➖ Subtraction
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

# ✖️ Multiplication
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

# ➗ Division
elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")

# ❌ If the user enters an unknown operator
else:
    print("Invalid operator!")

# 👋 Message after using the calculator
print("Thank you for using this calculator!")
