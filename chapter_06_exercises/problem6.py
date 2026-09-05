"""
📚 Topic: Chapter 06 Exercise - Problem 6

This script demonstrates chapter 06 exercise - problem 6 using user input,
conditions and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 06 exercise - problem 6
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 06 exercise - problem 6 affects the result.
"""


# 📝 Take marks from the user
marks = int(input("Enter your marks: "))

# 🚨 Check whether the marks are valid
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")

# 🏆 90 - 100 → Ex
elif marks >= 90:
    print("Ex")

# 🅰️ 80 - 89 → A
elif marks >= 80:
    print("A")

# 🅱️ 70 - 79 → B
elif marks >= 70:
    print("B")

# 🅲️ 60 - 69 → C
elif marks >= 60:
    print("C")

# 🅳️ 50 - 59 → D
elif marks >= 50:
    print("D")

# ❌ Below 50 → F
else:
    print("F")
