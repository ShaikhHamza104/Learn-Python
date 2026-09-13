"""
📚 Topic: Keyword Arguments

This script demonstrates keyword arguments using functions.

💡 Key points:
    1️⃣ the basic syntax for keyword arguments
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    keyword arguments affects the result.
"""


def sum(a, b, c, d):
    print(f"{a} + {b} + {c} + {d} = {a+b+c+d}")


sum(a=10, b=20, c=30, d=40)
