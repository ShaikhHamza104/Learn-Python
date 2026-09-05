"""
📚 Topic: Chapter 09 Exercise - Problem 8

This script demonstrates chapter 09 exercise - problem 8 using classes, file
or path operations and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 09 exercise - problem 8
    2️⃣ how classes fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 09 exercise - problem 8 affects the result.
"""


with open('this.txt', 'r')as f:
    data = f.read()

with open('this_copy.txt', 'w')as f:
    f.write(data)
