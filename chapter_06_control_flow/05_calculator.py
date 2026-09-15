"""
📚 Topic: Building a Basic Calculator with Conditionals

This script applies `if-elif-else` control flow to construct a simple
arithmetic calculator supporting addition, subtraction, multiplication,
and division.

💡 Key points:
    1️⃣ Converting user input strings to numeric values (`float`)
    2️⃣ Branching based on operator characters (`+`, `-`, `*`, `/`)
    3️⃣ Guarding against invalid operators with an `else` branch

🧠 Beginner tip:
    Always validate user inputs, especially when performing division, to
    prevent errors like `ZeroDivisionError`.
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
