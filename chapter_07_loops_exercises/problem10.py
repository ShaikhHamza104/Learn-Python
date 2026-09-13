"""
📚 Topic: Chapter 07 Exercise - Problem 10

This script demonstrates chapter 07 exercise - problem 10 using user input,
for loops and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 07 exercise - problem 10
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 07 exercise - problem 10 affects the result.
"""


# 🔢 Take a number from the user
num = int(input("Enter a number: "))

# 🔄 Loop from 10 down to 1
for i in range(10, 0, -1):
    # ✖️ Print the multiplication result
    print(f"{num} x {i} = {num * i}")
