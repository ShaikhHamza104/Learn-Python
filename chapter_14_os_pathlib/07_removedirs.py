"""
📚 Topic: Recursive Directory Removal (`os.removedirs()`)

This script demonstrates removing empty leaf and parent directories recursively
using `os.removedirs()`.

💡 Key points:
    1️⃣ Deleting leaf directory and parent directories if they become empty
    2️⃣ Stops when a non-empty directory is encountered
    3️⃣ Tidying up empty folder branches after file deletions

🧠 Beginner tip:
    `os.removedirs()` only deletes empty folders; files inside any parent
    halt removal safely.
"""


# importing os module : os module is a build in module
import os

# Removes an empty directory and its parent directories
try:
    os.removedirs("notes/c++")
    print("Directory and subdirectory deleted successfully")

except FileNotFoundError:
    print("Directory and subdirectory does not exists")
