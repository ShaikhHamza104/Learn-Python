"""
📚 Topic: Directory Listing with the OS Module

This exercise demonstrates querying the filesystem using Python's built-in `os`
module, retrieving entries inside a directory, and iterating over them.

💡 Key points:
    1️⃣ Importing the standard library `os` module
    2️⃣ Calling `os.listdir()` to retrieve directory contents as a list
    3️⃣ Iterating over directory entries using a `for` loop

🧠 Beginner tip:
    Using `"."` targets the current working directory portably across Windows,
    macOS, and Linux without hardcoding platform-specific paths.
"""


import os

# Inspect the current working directory
directory_path = "."

contents = os.listdir(directory_path)

for item in contents:
    print(item)
