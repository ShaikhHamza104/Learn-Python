"""
📚 Topic: Chapter 06 Exercise - Problem 3

This script demonstrates chapter 06 exercise - problem 3 using user input,
conditions and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 06 exercise - problem 3
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 06 exercise - problem 3 affects the result.
"""


# 🚨 Store the spam phrases
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

# 💬 Ask the user to enter a comment
comment = input("Enter your comment: ")

# 🔍 Check whether any spam phrase is present in the comment
if p1 in comment or p2 in comment or p3 in comment or p4 in comment:
    print("Spam is detected 🚨")

# ✅ If none of the spam phrases are found
else:
    print("This comment is not spam ✅")
