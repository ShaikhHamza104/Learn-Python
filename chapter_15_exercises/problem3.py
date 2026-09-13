"""
📚 Topic: Problem3

This script demonstrates problem3 using regex, functions and exception
handling.

💡 Key points:
    1️⃣ the basic syntax for problem3
    2️⃣ how regex fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem3 affects the result.
"""

import re


# 3. Write a program that hides every digit in a sentence by replacing
# it with a '#' symbol, using re.sub().
def hideNumbers():
    try:
        text = input("Enter a sentence with some numbers in it: ")
        hidden_text = re.sub(r"\d", "#", text)
        print("Result:", hidden_text)
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Input cancelled")


hideNumbers()
