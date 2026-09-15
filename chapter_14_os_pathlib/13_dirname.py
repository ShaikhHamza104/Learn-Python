"""
📚 Topic: Extracting Directory Names (`os.path.dirname()`)

This script demonstrates extracting parent directory paths from file paths
using `os.path.dirname()`.

💡 Key points:
    1️⃣ Extracting directory components from path strings
    2️⃣ Pairing with `os.path.basename()` to parse paths
    3️⃣ Determining script locations using `os.path.dirname(__file__)`

🧠 Beginner tip:
    `os.path.split(path)` returns a `(dirname, basename)` tuple in one call.
"""


# importing os module : os module is a build in module
import os

file_name = "05_makedirs.py"
# Returns the directory name of a path
a = os.path.dirname(file_name)
print(a)
a = os.path.getsize(file_name)
print(a)
