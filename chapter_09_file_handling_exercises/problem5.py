"""
📚 Topic: Chapter 09 Exercise - Problem 5

This script demonstrates chapter 09 exercise - problem 5 using for loops,
classes, file or path operations and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 09 exercise - problem 5
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 09 exercise - problem 5 affects the result.
"""


# . Repeat program 4 for a list of such words to be censored.
words = ["Donkey", "Bander", "Ganda", "Bekar"]
with open("problem4.txt") as f:
    data = f.read()
for word in words:
    data = data.replace(word, "#" * len(word))
with open("problem4.txt", 'w') as f:
    f.write(data)
