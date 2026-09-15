"""
📚 Topic: Opening & Reading Files

This script demonstrates opening, reading, and closing a plain text file using
Python's built-in `open()` function.

💡 Key points:
    1️⃣ `open('filename')` defaults to read mode (`'r'`)
    2️⃣ Reading entire contents with `f.read()`
    3️⃣ Explicitly closing file handles with `f.close()`

🧠 Beginner tip:
    Always close opened files to release operating system resources, or use
    the `with` statement for automatic cleanup.
"""
# Opening a file
f = open('sample.txt')  # default mode is r

# reading to a file
data = f.read()

# closeing to a file
f.close()
