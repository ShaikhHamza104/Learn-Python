"""
📚 Topic: Problem 5 - Modern Paths with Pathlib (Advanced)

This script demonstrates object-oriented file system paths using pathlib,
functions, and exception handling.

💡 Key points:
1️⃣ the syntax for creating Path objects instead of relying on string paths
2️⃣ how the rglob() method acts as a powerful recursive search tool
3️⃣ what to look for when iterating through complex nested directory trees

🧠 Beginner tip:
Pathlib is the modern replacement for many 'os' module functions. Notice
how `.resolve()` easily fetches the absolute path without needing 'os.path'.
"""

from pathlib import Path

# 5. Write a program using `pathlib` that searches the current directory
# and all subdirectories for any Python (.py) files,
# printing their absolute paths.


def find_py_files():
    try:
        current_path = Path(".")
        py_files = list(current_path.rglob("*.py"))
        if py_files:
            print("Python files found:")
            for file in py_files:
                print(file.resolve())
        else:
            print("No Python files found in the current directory"
                  " or subdirectories")
    except Exception as e:
        print("Error:", e)


find_py_files()
