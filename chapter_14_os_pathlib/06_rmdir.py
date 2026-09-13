"""
📚 Topic: 06 Rmdir

This script demonstrates 06 rmdir using exception handling and imports.

💡 Key points:
    1️⃣ the basic syntax for 06 rmdir
    2️⃣ how exception handling fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    06 rmdir affects the result.
"""

# importing os module : os module is a build in module
import os

# Removes an empty directory
try:
    os.rmdir("example")
    print("Directory deleted successfully")

except FileNotFoundError:
    print("Directory does not exists")
except OSError:
    print("The directory is not empty: 'example'")
