"""
📚 Topic: 13 Dirname

This script demonstrates 13 dirname using imports.

💡 Key points:
    1️⃣ the basic syntax for 13 dirname
    2️⃣ how imports fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    13 dirname affects the result.
"""

# importing os module : os module is a build in module
import os

file_name = "05_makedirs.py"
# Returns the directory name of a path
a = os.path.dirname(file_name)
print(a)
a = os.path.getsize(file_name)
print(a)
