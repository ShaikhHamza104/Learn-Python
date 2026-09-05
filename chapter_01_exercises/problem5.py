"""
📚 Topic: Chapter 01 Exercise - Problem 5

This script demonstrates chapter 01 exercise - problem 5 using for loops and
imports.

💡 Key points:
    1️⃣ the basic syntax for chapter 01 exercise - problem 5
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    chapter 01 exercise - problem 5 affects the result.
"""


# Q5. Write a python program to print the contents of a directory using the os
# module.
# Search online for the function which does that
import os

# Replace 'path_to_directory' with the path to the directory you want to print
directory_path = "/"

# List the contents of the directory
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)
