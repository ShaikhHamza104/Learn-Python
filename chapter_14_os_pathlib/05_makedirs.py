"""
📚 Topic: Recursive Directory Creation (`os.makedirs()`)

This script demonstrates creating nested directory hierarchies recursively
using `os.makedirs()`.

💡 Key points:
    1️⃣ Creating deep directory paths in one call (e.g. `a/b/c`)
    2️⃣ Setting `exist_ok=True` to prevent crashes when directories exist
    3️⃣ Safely preparing output folders for data export

🧠 Beginner tip:
    Always pass `exist_ok=True` to `os.makedirs()` for idempotent directory
    creation in production code.
"""


# importing os module : os module is a build in module
import os

# Creates a directory and its parent directories if they don't exist
try:
    os.makedirs("example/C/main.c")
    print("Directory created successfully")

except FileExistsError:
    print("Directory already exists")
