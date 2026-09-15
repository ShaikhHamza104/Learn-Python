"""
📚 Topic: Problem2

This script demonstrates problem2 using regex, functions and exception
handling.

💡 Key points:
    1️⃣ the basic syntax for problem2
    2️⃣ how regex fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem2 affects the result.
"""

import re


# 2. Write a program that checks if a phone number entered by the user
# is a valid 10-digit Indian phone number (starts with 6-9).
def validate_phone_number():
    try:
        phone = input("Enter your phone number: ")
        pattern = r"^[6-9]\d{9}$"

        if re.fullmatch(pattern, phone):
            print("Valid phone number ✅")
        else:
            print("Invalid phone number ❌")
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Input cancelled")


validate_phone_number()
