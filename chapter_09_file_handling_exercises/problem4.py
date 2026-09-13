"""
📚 Topic: Chapter 09 Exercise - Problem 4

This script demonstrates chapter 09 exercise - problem 4 using classes, file
or path operations and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 09 exercise - problem 4
    2️⃣ how classes fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 09 exercise - problem 4 affects the result.
"""


# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file.
with open('problem4.txt', 'r')as f:
    data = f.read()
    data = data.replace("Donkey", "#####")
    # data=data.replace("#####","Donkey")


with open('problem4.txt', 'w')as f:
    f.write(f"{data}")
