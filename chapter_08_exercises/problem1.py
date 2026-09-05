"""
📚 Topic: Chapter 08 Exercise - Problem 1

This script demonstrates chapter 08 exercise - problem 1 using conditions,
functions, classes and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 08 exercise - problem 1
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 08 exercise - problem 1 affects the result.
"""


def greatest(a, b, c):
    if a > b and a > c:
        return a

    elif b > a and b > c:
        return b

    else:
        return c


g = greatest(10, 89, 100)
print(g)
