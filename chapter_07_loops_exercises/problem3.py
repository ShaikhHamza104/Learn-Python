"""
📚 Topic: Chapter 07 Exercise - Problem 3

This script demonstrates chapter 07 exercise - problem 3 using user input,
while loops and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 07 exercise - problem 3
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 07 exercise - problem 3 affects the result.
"""


# 🔢 Take a number from the user
num = int(input("Enter a number: "))

# ▶️ Start the counter from 1
i = 1

# 🔄 Run the loop until i reaches 11
while i < 11:
    # ✖️ Print the multiplication result
    print(f"{num} x {i} = {num * i}")

    # ➕ Increase i by 1
    i += 1
