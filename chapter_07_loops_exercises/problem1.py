"""
📚 Topic: Chapter 07 Exercise - Problem 1

This script demonstrates chapter 07 exercise - problem 1 using user input,
for loops and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 07 exercise - problem 1
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 07 exercise - problem 1 affects the result.
"""


# 🔢 Take a number from the user
num = int(input("Enter a number: "))

# 🔄 Loop from 1 to 10
for i in range(1, 11):
    # ✖️ Multiply the given number by i
    # f-string makes the output easy to read
    print(f"{num} x {i} = {num * i}")
