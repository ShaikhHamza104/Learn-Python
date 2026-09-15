"""
📚 Topic: Checking If a Path Is a Regular File (`os.path.isfile()`)

This script demonstrates distinguishing regular files from directories or
special device nodes using `os.path.isfile()`.

💡 Key points:
    1️⃣ Verifying target path exists and is a regular file
    2️⃣ Returns `False` for directories, symlink targets, or missing paths
    3️⃣ Filtering directory listings for files only

🧠 Beginner tip:
    Use `os.path.isfile()` when you need to confirm that a path can be opened
    with `open()`.
"""


# importing os module : os module is a build in module
import os

try:
    os.chdir("example/c")
    file_name = "main.c"
    # Checks if a path is a file
    if os.path.isfile(file_name):
        print(f"File is detected: {file_name}")
    else:
        print(f"File is not detected: {file_name}")
except FileNotFoundError:
    print("Directory not found or file does not exist.")
except OSError as e:
    print(f"Error occurred: {e}")
