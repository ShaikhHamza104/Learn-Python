"""
📚 Topic: Changing Working Directories (`os.chdir()`)

This script demonstrates changing the process's active working directory using
`os.chdir()`.

💡 Key points:
    1️⃣ Modifying current working directory with `os.chdir(path)`
    2️⃣ Relative vs absolute destination paths
    3️⃣ Catching `FileNotFoundError` if the destination path does not exist

🧠 Beginner tip:
    Changing the working directory affects all subsequent relative file
    operations within the same Python process.
"""


# importing os module : os module is a build in module
import os

# Changes the current working directory
os.chdir(".")
