"""
📚 Topic: Chapter 07 Exercise - Problem 8

This script demonstrates chapter 07 exercise - problem 8 using for loops and
imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 07 exercise - problem 8
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 07 exercise - problem 8 affects the result.
"""


# 🔢 Define the number of rows
n = 3

# 🔄 Outer loop controls the rows
for i in range(1, n + 1):
    # ⭐ Inner loop prints '*' i times
    for j in range(i):
        print("*", end="")

    # ↩️ Move to the next line after printing the stars
    print()
