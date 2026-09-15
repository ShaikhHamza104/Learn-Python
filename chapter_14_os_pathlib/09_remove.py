"""
📚 Topic: Deleting Files (`os.remove()`)

This script demonstrates deleting files permanently from disk using
`os.remove()` (or `os.unlink()`).

💡 Key points:
    1️⃣ Permanently unlinking files from disk
    2️⃣ Raises `FileNotFoundError` if the file does not exist
    3️⃣ Raises `IsADirectoryError` if called on a directory

🧠 Beginner tip:
    `os.remove()` bypasses the operating system recycle bin / trash; deletions
    are permanent.
"""


# importing os module : os module is a build in module
import os

os.chdir("example/c")
file_name = "main.c"
files = []
try:
    # Deletes a file

    os.remove(file_name)
except PermissionError:
    print("You have not permition to delete a file")
