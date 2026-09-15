"""
📚 Topic: Listing Directory Contents (`os.listdir()`)

This script demonstrates inspecting files and directories present inside a
target directory using `os.listdir()`.

💡 Key points:
    1️⃣ Retrieving directory entries as a list of filename strings
    2️⃣ Passing `.` to inspect the current working directory
    3️⃣ Combining with loops to process files in bulk

🧠 Beginner tip:
    `os.listdir()` returns only entry names, not full paths; use
    `os.path.join()` or `pathlib.Path` to build complete paths.
"""


# importing os module : os module is a build in module
import os

# Returns a list of files and subdirectories in the specified path
print(os.listdir())
