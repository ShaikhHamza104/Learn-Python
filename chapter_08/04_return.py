"""
📚 Topic: Return Statement in Functions

This script demonstrates return statement in functions using functions and
user input.

💡 Key points:
    1️⃣ the basic syntax for return statement in functions
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    return statement in functions affects the result.
"""


def avg():
    a = int(input("Enter number : "))
    b = int(input("Enter number : "))
    c = int(input("Enter number : "))

    average = (a + b + c) / 2
    return average


a = avg()
print(a)
