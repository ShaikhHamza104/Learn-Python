"""
📚 Topic: File I/O Basics

This script demonstrates file i/o basics using file or path operations.

💡 Key points:
    1️⃣ the basic syntax for file i/o basics
    2️⃣ how file or path operations fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    file i/o basics affects the result.
"""


# Opening a file
f = open('sample.txt')  # default mode is r

# reading to a file
data = f.read()

# closeing to a file
f.close()
