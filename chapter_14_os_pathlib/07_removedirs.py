"""
📚 Topic: 07 Removedirs

This script demonstrates 07 removedirs using exception handling and imports.

💡 Key points:
    1️⃣ the basic syntax for 07 removedirs
    2️⃣ how exception handling fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    07 removedirs affects the result.
"""

# importing os module : os module is a build in module
import os

# Removes an empty directory and its parent directories
try:
    os.removedirs("notes/c++")
    print("Directory and subdirectory deleted successfully")

except FileNotFoundError:
    print("Directory and subdirectory does not exists")
