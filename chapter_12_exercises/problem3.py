"""
📚 Topic: Problem3

This script demonstrates problem3 using user input, for loops, conditions
and exception handling.

💡 Key points:
    1️⃣ the basic syntax for problem3
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem3 affects the result.
"""

# Write a function that opens and reads a filename. Use try, except, and else
# to handle the file operation and print successful reads.
import os

d = os.listdir()
for file in d:
    print(file)
try:
    file_name = input("Enter a file name ")
    f = open(file_name)
except FileNotFoundError:
    print("This file name has not present in this directroy")
