"""
📚 Topic: The `return` Statement

This script demonstrates returning computed values from functions back to the
caller.

💡 Key points:
    1️⃣ Using `return` to pass calculation results to the calling context
    2️⃣ Assigning returned values to variables or nesting inside expressions
    3️⃣ Functions without an explicit `return` implicitly return `None`

🧠 Beginner tip:
    `print()` merely shows output on screen; `return` gives the result back
    to the program for further calculation.
"""


def avg():
    a = int(input("Enter number : "))
    b = int(input("Enter number : "))
    c = int(input("Enter number : "))

    average = (a + b + c) / 2
    return average


a = avg()
print(a)
