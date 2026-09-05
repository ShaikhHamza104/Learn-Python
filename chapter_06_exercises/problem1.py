"""
📚 Topic: Chapter 06 Exercise - Problem 1

This script demonstrates chapter 06 exercise - problem 1 using user input,
conditions and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 06 exercise - problem 1
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 06 exercise - problem 1 affects the result.
"""


# ═══════════════════════════════════════
# 🥇 SOLUTION 1: Using if-elif
# ═══════════════════════════════════════

# 🔢 Take four numbers from the user
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

# 🔍 Check if num1 is greater than all other numbers
if num1 > num2 and num1 > num3 and num1 > num4:
    print("Number 1 is greater:", num1)

# 🔍 Check if num2 is greater than all other numbers
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("Number 2 is greater:", num2)

# 🔍 Check if num3 is greater than all other numbers
elif num3 > num1 and num3 > num2 and num3 > num4:
    print("Number 3 is greater:", num3)

# 🔍 Check if num4 is greater than all other numbers
elif num4 > num1 and num4 > num2 and num4 > num3:
    print("Number 4 is greater:", num4)


# ═══════════════════════════════════════
# 🥈 SOLUTION 2: Using list and max()
# ═══════════════════════════════════════

# 📦 Create an empty list
greater = []

# 🔢 Take four numbers from the user
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

# 📥 Add all four numbers to the list
greater.extend([num1, num2, num3, num4])

# 🏆 Find and print the greatest number
print("Greatest number is:", max(greater))
