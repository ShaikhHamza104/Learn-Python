"""
📚 Topic: Problem7

This script demonstrates problem7 using user input, conditions, functions
and classes.

💡 Key points:
    1️⃣ the basic syntax for problem7
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem7 affects the result.
"""


# Define NegativeValueError and raise it when a function receives a negative
# number.
class NegativeValueError(Exception):
    pass


def acceptPositiveValue(n):
    if n < 0:
        raise NegativeValueError


try:
    n = int(input("Enter a number : "))
    acceptPositiveValue(n)
except NegativeValueError:
    print("Please Enter positive Number")
