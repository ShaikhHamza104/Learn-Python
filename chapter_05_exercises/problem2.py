"""
📚 Topic: Chapter 05 Exercise - Problem 2

This script demonstrates chapter 05 exercise - problem 2 using user input
and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 05 exercise - problem 2
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 05 exercise - problem 2 affects the result.
"""


# 🧺 Create an empty set
# We will store all the numbers entered by the user in this set.
s = set()


# 1️⃣ Take the first number from the user
num1 = int(input("Enter number 1 : "))


# 2️⃣ Take the second number from the user
num2 = int(input("Enter number 2 : "))


# 3️⃣ Take the third number from the user
num3 = int(input("Enter number 3 : "))


# 4️⃣ Take the fourth number from the user
num4 = int(input("Enter number 4 : "))


# 5️⃣ Take the fifth number from the user
num5 = int(input("Enter number 5 : "))


# 6️⃣ Take the sixth number from the user
num6 = int(input("Enter number 6 : "))


# 7️⃣ Take the seventh number from the user
num7 = int(input("Enter number 7 : "))


# 8️⃣ Take the eighth number from the user
num8 = int(input("Enter number 8 : "))


# ➕ Add all eight numbers to the set
# update() adds multiple elements to the set at once.
#
# 💡 If a number is repeated, the set automatically keeps
# only one copy of that number.
s.update({num1, num2, num3, num4, num5, num6, num7, num8})


# 📋 Display all unique numbers
print(s)

# Example:
# If the user enters:
# 10, 20, 10, 30, 20, 40, 50, 10
#
# Output:
# {10, 20, 30, 40, 50}
