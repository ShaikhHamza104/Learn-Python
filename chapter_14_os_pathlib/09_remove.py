"""
📚 Topic: 09 Remove

This script demonstrates 09 remove using exception handling and imports.

💡 Key points:
    1️⃣ the basic syntax for 09 remove
    2️⃣ how exception handling fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    09 remove affects the result.
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
