"""
📚 Topic: Chapter 01 Exercise - Problem 4

This script demonstrates chapter 01 exercise - problem 4 using for loops and
imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 01 exercise - problem 4
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 01 exercise - problem 4 affects the result.
"""


# Q4. Write a python program to print the contents of a directory using the os
# module.
# Search online for the function which does that
import os

directory_path = "/"

contents = os.listdir(directory_path)

for item in contents:
    print(item)
