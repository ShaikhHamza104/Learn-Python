"""
📚 Topic: 04 Mkdir

This script demonstrates 04 mkdir using exception handling and imports.

💡 Key points:
    1️⃣ the basic syntax for 04 mkdir
    2️⃣ how exception handling fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    04 mkdir affects the result.
"""

# importing os module : os module is a build in module
import os

# Creates a new directory
try:
    os.mkdir("example")
    print("Directory created successfully")

except FileExistsError:
    print("Directory already exists")
