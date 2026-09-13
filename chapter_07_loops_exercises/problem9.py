"""
📚 Topic: Chapter 07 Exercise - Problem 9

This script demonstrates chapter 07 exercise - problem 9 using user input,
for loops, conditions and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 07 exercise - problem 9
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 07 exercise - problem 9 affects the result.
"""


# 🔢 Take the number of rows from the user
n = int(input("Enter a number: "))

# 🔄 Loop through each row
for i in range(1, n + 1):
    # ⭐ First and last rows contain n stars
    if i == 1 or i == n:
        print("* " * n)

    # ⭐ Middle rows contain stars at both ends
    else:
        print("*" + " " * (2 * n - 3) + "*")
