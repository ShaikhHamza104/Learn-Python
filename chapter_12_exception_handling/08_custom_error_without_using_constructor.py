"""
📚 Topic: 08 Custom Error Without Using Constructor

This script demonstrates 08 custom error without using constructor using
user input, conditions, classes and exception handling.

💡 Key points:
    1️⃣ the basic syntax for 08 custom error without using constructor
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    08 custom error without using constructor affects the result.
"""


class InvalidAge(Exception):
    pass


try:
    age = int(input("Enter your age : "))
    if age < 18:
        raise InvalidAge
except InvalidAge:
    print("Age should not be less then 18 ")
