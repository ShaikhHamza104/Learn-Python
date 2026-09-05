"""
📚 Topic: 11 Isfile

This script demonstrates 11 isfile using conditions, exception handling and
imports.

💡 Key points:
    1️⃣ the basic syntax for 11 isfile
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    11 isfile affects the result.
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
