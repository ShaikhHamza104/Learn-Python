"""
📚 Topic: Chapter 08 Exercise - Problem 4

This script demonstrates chapter 08 exercise - problem 4 using user input,
conditions, functions and classes.

💡 Key points:
    1️⃣ the basic syntax for chapter 08 exercise - problem 4
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 08 exercise - problem 4 affects the result.
"""


def sum(n):
    if n == 1:
        return 1
    return sum(n - 1) + n


n = int(input("Enter a number : "))
print(sum(n))
