"""
📚 Topic: Chapter 09 Exercise - Problem 9

This script demonstrates chapter 09 exercise - problem 9 using conditions,
classes, file or path operations and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 09 exercise - problem 9
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 09 exercise - problem 9 affects the result.
"""


# Write a program to find out whether a file is identical & matches the content
# of
# another file.

with open('file1.txt') as f:
    data1 = f.read()

with open('file2.txt') as f:
    data2 = f.read()

if data1 == data2:
    print("Yes this file are identical")
else:
    print("No this file are identical")
