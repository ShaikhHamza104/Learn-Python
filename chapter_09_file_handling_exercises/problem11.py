"""
📚 Topic: Chapter 09 Exercise - Problem 11

Rename a file by copying its content to a new filename and deleting original.

💡 Key points:
    1️⃣ Reading data from the original file
    2️⃣ Writing content to the renamed file target
    3️⃣ Deleting the original file using `os.remove()`
"""
# . Write a python program to rename a file to “renamed_by_ python.txt.
with open('file1.txt') as f:
    data = f.read()
