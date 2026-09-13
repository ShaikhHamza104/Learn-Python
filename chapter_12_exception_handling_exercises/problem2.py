"""
📚 Topic: Problem2

This script demonstrates problem2 using user input, for loops, functions and
exception handling.

💡 Key points:
    1️⃣ the basic syntax for problem2
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem2 affects the result.
"""


# Prompt for two numbers and perform division. Use separate except blocks
# for ZeroDivisionError and ValueError.


def divisionOfTwoNumber(a: int, b):
    return a / b


try:
    a = int(input("Enter a first number : "))
    b = int(input("Enter a second number : "))
    divisionOfTwoNumber(a, b)
except ValueError:
    print("Check input")
except ZeroDivisionError:
    print("You cannot dived any number by zero ")
