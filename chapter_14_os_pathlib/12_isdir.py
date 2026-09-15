"""
📚 Topic: Checking If a Path Is a Directory (`os.path.isdir()`)

This script demonstrates testing whether a given filesystem path is a
directory.

💡 Key points:
    1️⃣ Verifying whether a path points to an existing directory
    2️⃣ Returns `False` for files or non-existent paths
    3️⃣ Navigating directory trees conditionally

🧠 Beginner tip:
    Use `os.path.isdir()` to separate folders from files when processing
    `os.listdir()` entries.
"""


# importing os module : os module is a build in module
import os

try:
    os.chdir("example")
    dir_name = "c"
    # Checks if a path is a directory
    if os.path.isdir(dir_name):
        print(f"directory is detected: {dir_name}")
    else:
        print(f"directory is not detected: {dir_name}")
except FileNotFoundError:
    print("Directory not found or file does not exist.")
except OSError as e:
    print(f"Error occurred: {e}")
