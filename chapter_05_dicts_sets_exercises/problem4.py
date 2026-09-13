"""
📚 Topic: Chapter 05 Exercise - Problem 4

This script demonstrates chapter 05 exercise - problem 4 using imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 05 exercise - problem 4
    2️⃣ how imports fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 05 exercise - problem 4 affects the result.
"""


# 🧺 Create an empty set
s = set()


# ➕ Add an integer
s.add(20)


# ➕ Add a float
# 20.0 is considered equal to 20 in Python,
# so the set will not store it as a separate value.
s.add(20.0)


# ➕ Add a string
# "20" is different from the number 20,
# so it will be stored separately.
s.add("20")


# 📏 Find the number of unique values in the set
print(len(s))

# Output:
# 2
