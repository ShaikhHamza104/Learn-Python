"""
📚 Topic: Chapter 07 Exercise - Problem 2

This script demonstrates chapter 07 exercise - problem 2 using for loops,
conditions and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 07 exercise - problem 2
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 07 exercise - problem 2 affects the result.
"""

# 📋 Store names in a list
l = ["Harry", "Soham", "Sachin", "Rahul"]  # noqa: E741

# 🔄 Check each name in the list
for name in l:
    # 🔍 Check if the name starts with the letter "S"
    if name.startswith("S"):
        # 👋 Greet the person
        print("Greeting " + name)
