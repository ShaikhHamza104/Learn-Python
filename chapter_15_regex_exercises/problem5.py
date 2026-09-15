"""
📚 Topic: Problem5

This script demonstrates problem5 using regex, functions and exception
handling.

💡 Key points:
1️⃣ the basic syntax for problem5
2️⃣ how regex fit into the example
3️⃣ what to look for when you run the file

🧠 Beginner tip:
Run this file, change one small value, and run it again to see how
problem5 affects the result.
"""

import re

# 5. Write a program that checks if a password entered by the user is
# strong: at least 8 characters, one uppercase letter, one digit,
# and one special character.


def check_password_strength():
    try:
        password = input("Enter a password: ")

        has_length = len(password) >= 8
        has_upper = re.search(r"[A-Z]", password) is not None
        has_digit = re.search(r"\d", password) is not None
        has_special = re.search(r"[^A-Za-z0-9]", password) is not None

        if has_length and has_upper and has_digit and has_special:
            print("Strong password ✅")
        else:
            print(
                "Weak password ❌ - needs 8+ chars, "
                "1 uppercase, 1 digit, and 1 special character"
            )

    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Input cancelled")


check_password_strength()
