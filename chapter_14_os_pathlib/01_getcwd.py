"""
📚 Topic: Current Working Directory (`os.getcwd()`)

This script demonstrates retrieving the current working directory path using
Python's standard `os` module.

💡 Key points:
    1️⃣ Calling `os.getcwd()` returns the active working directory as a string
    2️⃣ Difference between script location and working directory
    3️⃣ Using absolute paths to prevent relative path ambiguity

🧠 Beginner tip:
    The current working directory is where Python was launched from, which may
    differ from the directory containing the running `.py` script.
"""


# importing os module : os module is a build in module
import os

# Returns the current working directory
print(os.getcwd())
