"""
📚 Topic: Chapter 09 Exercise - Problem 6

This script demonstrates chapter 09 exercise - problem 6 using conditions,
classes, file or path operations and imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 09 exercise - problem 6
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 09 exercise - problem 6 affects the result.
"""


# Write a program to mine a log file and find out whether it contains ‘python’.
with open("log.txt") as f:
    data = f.read()
    if "Python".lower() in data.lower():
        print("Yes files contains 'Python'")
    else:
        print("no files contains 'Python'")
