"""
📚 Topic: Problem8

This script demonstrates problem8 using user input, conditions, classes and
exception handling.

💡 Key points:
    1️⃣ the basic syntax for problem8
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem8 affects the result.
"""


# Define InvalidAgeError without a constructor. Raise it for an age below 0
# or above 150.
class InvalidAgeError(Exception):
    pass


try:
    user_age = int(input("Enter your age: "))
    if user_age <= 0 or user_age > 150:
        raise InvalidAgeError
except InvalidAgeError:
    print("Age must be grater then 0 or less 150")
