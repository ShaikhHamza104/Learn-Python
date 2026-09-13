"""
📚 Topic: 07 Raise Error

This script demonstrates 07 raise error using user input, conditions and
exception handling.

💡 Key points:
    1️⃣ the basic syntax for 07 raise error
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    07 raise error affects the result.
"""


try:
    age = int(input("Enter your age "))
    if age < 18:
        raise ValueError
except ValueError:
    print("Your age is less then 18 ")
