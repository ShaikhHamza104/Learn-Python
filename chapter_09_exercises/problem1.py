"""
📚 Topic: Chapter 09 Exercise - Problem 1

This script demonstrates chapter 09 exercise - problem 1 using conditions,
classes, file or path operations and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 09 exercise - problem 1
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 09 exercise - problem 1 affects the result.
"""


# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.
with open("poems.txt") as f:
    data = f.read()
    if 'twinkle' in data:
        print("file contain 'Twinkle' ")
