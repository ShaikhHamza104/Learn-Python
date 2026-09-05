"""
📚 Topic: Problem1

This script demonstrates problem1 using user input, conditions, functions
and exception handling.

💡 Key points:
    1️⃣ the basic syntax for problem1
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem1 affects the result.
"""


# 1. Write a program that takes integer input and raises ValueError
# if the input is not an integer.
def inputAsInteger():
    try:
        int(input("Enter any number "))
    except ValueError as e:
        print(e)


inputAsInteger()
