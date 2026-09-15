"""
📚 Topic: Retrieving File Sizes (`os.path.getsize()`)

This script demonstrates inspecting file sizes in bytes using
`os.path.getsize()`.

💡 Key points:
    1️⃣ Measuring file size in bytes
    2️⃣ Converting raw byte counts to kilobytes, megabytes, or gigabytes
    3️⃣ Raising `FileNotFoundError` if the target path is missing

🧠 Beginner tip:
    Divide bytes by 1024 to convert to KB, or by `1024 ** 2` to convert to MB.
"""


# importing os module : os module is a build in module
import os

file_name = "05_makedirs.py"
# Returns the size of a file
a = os.path.getsize(file_name)  # 297
print(a)
