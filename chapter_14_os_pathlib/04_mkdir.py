"""
📚 Topic: Creating Directories (`os.mkdir()`)

This script demonstrates creating new single-level directories with
`os.mkdir()`.

💡 Key points:
    1️⃣ Creating a single directory path
    2️⃣ Raises `FileExistsError` if the directory already exists
    3️⃣ Raises `FileNotFoundError` if intermediate parents do not exist

🧠 Beginner tip:
    To create nested parent directories without error, use `os.makedirs()`.
"""


# importing os module : os module is a build in module
import os

# Creates a new directory
try:
    os.mkdir("example")
    print("Directory created successfully")

except FileExistsError:
    print("Directory already exists")
