"""
📚 Topic: Chapter 05 Exercise - Problem 7

This script demonstrates chapter 05 exercise - problem 7 using imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 05 exercise - problem 7
    2️⃣ how imports fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 05 exercise - problem 7 affects the result.
"""

# 📚 Create a dictionary containing friends and their
# favorite programming languages.
laguage = {
    "Rahul": "Php",
    "Harry": "Python",
    "Hamza": "Datascience",
}

# ⚠️ A repeated key replaces its earlier value.
laguage["Harry"] = "Django"


# 📋 Display the final dictionary
print(laguage)

# Output:
# {'Rahul': 'Php', 'Harry': 'Django', 'Hamza': 'Datascience'}


# 💡 Important:
# Dictionary keys must be unique.
#
# If the same key is used again:
#
# "Harry": "Python"
# "Harry": "Django"
#
# Python keeps only:
#
# "Harry": "Django"
#
# The latest value replaces the previous value.
