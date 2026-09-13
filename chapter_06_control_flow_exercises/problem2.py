"""
📚 Topic: Chapter 06 Exercise - Problem 2

This script demonstrates chapter 06 exercise - problem 2 using user input,
for loops, conditions and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 06 exercise - problem 2
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 06 exercise - problem 2 affects the result.
"""


# 📝 Take marks for the three subjects
mark1 = int(input("Enter your mark for Subject 1: "))
mark2 = int(input("Enter your mark for Subject 2: "))
mark3 = int(input("Enter your mark for Subject 3: "))

# 📊 Calculate total percentage
# Each subject has 100 marks, so total marks = 300
percentage = (100 * (mark1 + mark2 + mark3)) / 300

# 🔍 Check total percentage AND marks in every subject
if percentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33:
    print("You are passed 🎉", percentage, "%")

# ❌ If any condition is False, the student fails
else:
    print("You failed. Try again next year 📚", percentage, "%")
