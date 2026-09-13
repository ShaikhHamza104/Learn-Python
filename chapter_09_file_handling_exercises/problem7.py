"""
📚 Topic: Chapter 09 Exercise - Problem 7

This script demonstrates chapter 09 exercise - problem 7 using for loops,
conditions, classes and file or path operations.

💡 Key points:
    1️⃣ the basic syntax for chapter 09 exercise - problem 7
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 09 exercise - problem 7 affects the result.
"""


# Write a program to find out the line number where python is present from ques
# 6.
with open("log.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if "Python" in line:
        print(f"Yes python is present on line no {lineno}")
        break
    lineno += 1
else:
    print("Python is not present yet")
