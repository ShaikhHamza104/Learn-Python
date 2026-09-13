"""
📚 Topic: Chapter 07 Exercise - Problem 6

This script demonstrates chapter 07 exercise - problem 6 using user input,
for loops and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 07 exercise - problem 6
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 07 exercise - problem 6 affects the result.
"""


# 🔢 Take a number from the user
num = int(input("Enter number: "))

# 📦 Start the factorial result with 1
fact = 1

# 🔄 Loop from 1 to num
for i in range(1, num + 1):
    # ✖️ Multiply the current result by i
    fact = fact * i

# ✅ Display the final factorial
print(f"Factorial of {num} is {fact}")
