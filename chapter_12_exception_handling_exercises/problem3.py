"""
📚 Topic: Chapter 12 Exercise - Problem 3

Access list elements by index and handle `IndexError` for invalid
requests.

💡 Key points:
    1️⃣ Indexing lists dynamically
    2️⃣ Catching `IndexError` when requested index exceeds list length
    3️⃣ Safeguarding sequence access
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
