"""
📚 Topic: Chapter 09 Exercise - Problem 3

This script demonstrates chapter 09 exercise - problem 3 using for loops,
functions, classes and file or path operations.

💡 Key points:
    1️⃣ the basic syntax for chapter 09 exercise - problem 3
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 09 exercise - problem 3 affects the result.
"""


import os
dr = os.chdir('chapter 9 pr/table')


def function():
    n = 21
    for i in range(2, n):
        with open(f"table{i}.txt", 'a') as f:
            for j in range(1, 11):
                f.write(f"{i} × {j} = {i * j}\n")


function()
