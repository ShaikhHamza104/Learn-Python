"""
📚 Topic: Lambda (Anonymous) Functions

This script demonstrates short, anonymous functions defined inline using the
`lambda` keyword.

💡 Key points:
    1️⃣ Syntax: `lambda arguments: expression`
    2️⃣ Single-expression restriction without multi-line statements
    3️⃣ Passing lightweight inline functions to higher-order helpers

🧠 Beginner tip:
    Use `def` for complex or named functions; use `lambda` for quick one-off
    operations like sorting keys.
"""


# 1️⃣ Define a lambda function to compute the square of a number
square = lambda x: x * x  # noqa: E731

n = int(input("Enter number do you want to find square : "))
print(f"Square of {n}: {square(n)}")

# 2️⃣ Define a lambda function to compute the cube of a number
cube = lambda x: x * x * x  # noqa: E731

n = int(input("Enter number do you want to find cube : "))
print(f"Cube of {n}: {cube(n)}")

# 3️⃣ Using lambda inline without binding to a name
numbers = [1, 2, 3, 4, 5]
squared_list = list(map(lambda val: val ** 2, numbers))
print(f"Squared list using inline lambda: {squared_list}")
