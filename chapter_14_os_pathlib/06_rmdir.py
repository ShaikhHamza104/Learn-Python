"""
📚 Topic: Removing Empty Directories (`os.rmdir()`)

This script demonstrates deleting empty directories using `os.rmdir()`.

💡 Key points:
    1️⃣ Deleting a single empty directory
    2️⃣ Raises `OSError` if the directory contains any files or subfolders
    3️⃣ Safe cleanup that protects against accidental data destruction

🧠 Beginner tip:
    To delete non-empty directories recursively, use `shutil.rmtree()`.
"""


# importing os module : os module is a build in module
import os

# Removes an empty directory
try:
    os.rmdir("example")
    print("Directory deleted successfully")

except FileNotFoundError:
    print("Directory does not exists")
except OSError:
    print("The directory is not empty: 'example'")
