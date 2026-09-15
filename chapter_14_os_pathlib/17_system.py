"""
📚 Topic: Running Shell Commands (`os.system()`)

This script demonstrates executing operating system shell commands from Python
using `os.system()`.

💡 Key points:
    1️⃣ Passing shell command strings to the underlying OS
    2️⃣ Returns process exit status code (0 usually indicates success)
    3️⃣ Awareness: modern code prefers the `subprocess` standard module

🧠 Beginner tip:
    `os.system()` is legacy; use `subprocess.run()` for robust input/output
    handling and security.
"""


# importing os module : os module is a build in module
import os

#  Executes a command in a subshell and returns the exit status.
os.system("dir")
