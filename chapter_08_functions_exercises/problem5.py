"""
📚 Topic: Chapter 08 Exercise - Problem 5

This script demonstrates chapter 08 exercise - problem 5 using conditions,
functions, classes and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 08 exercise - problem 5
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 08 exercise - problem 5 affects the result.
"""


def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n - 1)


pattern(3)
