"""
📚 Topic: 12 Isdir

This script demonstrates 12 isdir using conditions, exception handling and
imports.

💡 Key points:
    1️⃣ the basic syntax for 12 isdir
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    12 isdir affects the result.
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
