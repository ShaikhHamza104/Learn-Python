"""
📚 Topic: Chapter 06 Exercise - Problem 7

This script demonstrates chapter 06 exercise - problem 7 using user input,
for loops, conditions and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 06 exercise - problem 7
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 06 exercise - problem 7 affects the result.
"""


# 👤 Store the name we want to search for
name = "Harry"

# 💬 Ask the user to enter their post
post = input("Enter your post: ")

# 🔍 Check whether "Harry" is present in the post
# 🔤 lower() makes the search case-insensitive
if name.lower() in post.lower():
    print('This post is talking about "Harry"')

# ❌ If Harry is not mentioned
else:
    print('This post is not talking about "Harry"')
