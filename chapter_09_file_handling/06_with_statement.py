"""
📚 Topic: The with Statement

This script demonstrates the with statement using file or path operations.

💡 Key points:
    1️⃣ the basic syntax for the with statement
    2️⃣ how file or path operations fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    the with statement affects the result.
"""


with open('sample.txt') as f:
    print(f.read())
