"""
📚 Topic: Chapter 05 Exercise - Problem 8

This script demonstrates chapter 05 exercise - problem 8 using imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 05 exercise - problem 8
    2️⃣ how imports fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 05 exercise - problem 8 affects the result.
"""

# 📚 Create a dictionary containing friends and their
# favorite programming languages.
laguage = {
    "Rahul": "Php",
    "Harry": "Python",
    # ✅ "Python" is already used as a value by Harry,
    # but duplicate values are allowed in a dictionary.
    "Hamza": "Python",
}

# ⚠️ A repeated key replaces its earlier value.
laguage["Rahul"] = "Django"


# 📋 Display the final dictionary
print(laguage)

# Output:
# {'Rahul': 'Django', 'Harry': 'Python', 'Hamza': 'Python'}


# 💡 Remember:
#
# Dictionary keys  → Must be unique ❌ duplicate keys are not allowed
# Dictionary values → Can be repeated ✅ duplicate values are allowed
#
# Example:
#
# "Harry": "Python"
# "Hamza": "Python"
#
# This is completely valid because "Harry" and "Hamza"
# are two different keys.
