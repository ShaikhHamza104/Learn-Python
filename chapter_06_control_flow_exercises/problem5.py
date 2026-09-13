"""
📚 Topic: Chapter 06 Exercise - Problem 5

This script demonstrates chapter 06 exercise - problem 5 using user input,
for loops, conditions and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 06 exercise - problem 5
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 06 exercise - problem 5 affects the result.
"""


# 📋 Create a list of names
list_of_name = ["Rohit", "Rajo", "Harry", "Hamza"]

# 👤 Ask the user for their name
# 🔤 capitalize() makes the first letter uppercase
name = input("Enter your name: ").capitalize()

# 🔍 Check whether the name exists in the list
if name in list_of_name:
    print("Your name is in the list ✅")

# ❌ Name is not present in the list
else:
    print("Your name is not in the list ❌")
