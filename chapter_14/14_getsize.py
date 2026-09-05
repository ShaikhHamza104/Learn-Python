"""
📚 Topic: 14 Getsize

This script demonstrates 14 getsize using imports.

💡 Key points:
    1️⃣ the basic syntax for 14 getsize
    2️⃣ how imports fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    14 getsize affects the result.
"""

# importing os module : os module is a build in module
import os

file_name = "05_makedirs.py"
# Returns the size of a file
a = os.path.getsize(file_name)  # 297
print(a)
