"""
📚 Topic: Chapter 08 Exercise - Problem 8

This script demonstrates chapter 08 exercise - problem 8 using user input,
for loops, functions and classes.

💡 Key points:
    1️⃣ the basic syntax for chapter 08 exercise - problem 8
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 08 exercise - problem 8 affects the result.
"""


def multiplication(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")


num = int(input("Enter a number "))
multiplication(num)
