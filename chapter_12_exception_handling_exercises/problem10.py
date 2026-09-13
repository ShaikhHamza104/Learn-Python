"""
📚 Topic: Problem10

This script demonstrates problem10 using user input, conditions, functions
and exception handling.

💡 Key points:
    1️⃣ the basic syntax for problem10
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem10 affects the result.
"""


# Prompt for two numbers and perform division. Handle ZeroDivisionError
# and allow the user to exit with a specific keyword.
def divding_by_0():
    try:
        a = int(input("Enter a first number: "))
        b = int(input("Enter a second number: "))
        d = a / b
    except ZeroDivisionError:
        print(f"You can {a} by deviding by 0")
    else:
        print(f"Division of deviding {a} by {b} is {d}")


divding_by_0()
