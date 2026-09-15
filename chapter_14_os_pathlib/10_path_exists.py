"""
📚 Topic: Checking Path Existence (`os.path.exists()`)

This script demonstrates verifying whether a file or directory exists before
performing operations.

💡 Key points:
    1️⃣ Testing path existence returning boolean `True` or `False`
    2️⃣ Works for both files and directory paths
    3️⃣ Preventing `FileNotFoundError` in read/write workflows

🧠 Beginner tip:
    In modern code, `pathlib.Path("file.txt").exists()` is preferred for
    readability.
"""


# importing os module : os module is a build in module
import os

os.chdir("example/c")

file_name = "main.c"

# Checks if a path exists
if os.path.exists("main.c"):
    print(f"Yes, {file_name} file is exists")
else:
    print(f"No, {file_name} file is exists")
