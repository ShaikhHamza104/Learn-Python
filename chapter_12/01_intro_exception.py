"""
📚 Topic: 01 Intro Exception

This script demonstrates 01 intro exception using user input, conditions and
exception handling.

💡 Key points:
    1️⃣ the basic syntax for 01 intro exception
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    01 intro exception affects the result.
"""


# This code generates an error for text, names, characters, or float input.
# a=int(input("Enter a number : "))

try:
    a = int(input("Enter a number : "))
except ValueError:
    print("Error !! Please enter a valid number ")
