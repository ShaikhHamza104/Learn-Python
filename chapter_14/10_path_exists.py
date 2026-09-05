"""
📚 Topic: 10 Path Exists

This script demonstrates 10 path exists using conditions and imports.

💡 Key points:
    1️⃣ the basic syntax for 10 path exists
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    10 path exists affects the result.
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
