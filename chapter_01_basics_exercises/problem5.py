"""
📚 Topic: Labeled Directory Traversal with Comments

This exercise reinforces reading local directory trees using `os.listdir()`
with descriptive explanatory comments following clean coding practices.

💡 Key points:
    1️⃣ Reading filesystem directory contents via `os.listdir()`
    2️⃣ Documenting script steps clearly with informative comments
    3️⃣ Iterating and printing individual directory entries

🧠 Beginner tip:
    `os.listdir()` returns filenames and subdirectory names as plain strings;
    it does not recurse into nested subfolders automatically.
"""


import os

# Inspect the current directory portably
directory_path = "."

# List the contents of the directory
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)
