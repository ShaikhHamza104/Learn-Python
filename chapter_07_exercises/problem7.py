"""
📚 Topic: Chapter 07 Exercise - Problem 7

This script demonstrates chapter 07 exercise - problem 7 using user input,
for loops and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 07 exercise - problem 7
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 07 exercise - problem 7 affects the result.
"""


# 🔢 Take the number of rows from the user
n = int(input("Enter a number: "))

# 🔄 Create each row of the pattern
for i in range(1, n + 1):

    # ⬜ Print spaces before the stars
    # `end=""` prevents moving to the next line
    print(" " * (n - i), end="")

    # ⭐ Print the required number of stars
    print("*" * (2 * i - 1), end="")

    # ↩️ Move to the next line
    print("")
