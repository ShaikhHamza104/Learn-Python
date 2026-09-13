"""
📚 Topic: 05 Makedirs

This script demonstrates 05 makedirs using conditions, exception handling
and imports.

💡 Key points:
    1️⃣ the basic syntax for 05 makedirs
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    05 makedirs affects the result.
"""

# importing os module : os module is a build in module
import os

# Creates a directory and its parent directories if they don't exist
try:
    os.makedirs("example/C/main.c")
    print("Directory created successfully")

except FileExistsError:
    print("Directory already exists")
