"""
📚 Topic: Recursion in Python

This script demonstrates recursion in python using functions, conditions and
user input.

💡 Key points:
    1️⃣ the basic syntax for recursion in python
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    recursion in python affects the result.
"""


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input("Enter a number : "))
print(f"The factorial of {n} is {factorial(n)}")
