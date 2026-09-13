"""
📚 Topic: 05 File Handing

This script demonstrates 05 file handing using user input, conditions,
exception handling and file or path operations.

💡 Key points:
    1️⃣ the basic syntax for 05 file handing
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    05 file handing affects the result.
"""


try:
    file = input("Enter file name you want to open ")
    f = open(file)
except FileNotFoundError:
    print(f"{file} not found Error")
else:
    data = f.read()
    print(data)
finally:
    f.close()
