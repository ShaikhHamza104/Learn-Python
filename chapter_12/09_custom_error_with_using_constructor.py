"""
📚 Topic: 09 Custom Error With Using Constructor

This script demonstrates 09 custom error with using constructor using user
input, conditions, functions and classes.

💡 Key points:
    1️⃣ the basic syntax for 09 custom error with using constructor
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    09 custom error with using constructor affects the result.
"""


class InvalidPass(Exception):
    def __init__(self, msg):
        self.error_massage = msg


try:
    password = input("Enter a password: ")
    if not password.isalnum() or len(password) < 10:
        raise InvalidPass(
            "Password must contain at least 10 letters or digits and "
            "must not use special characters."
        )
except InvalidPass as e:
    print(e)
