"""
📚 Topic: Problem5

This script demonstrates problem5 using user input, exception handling, file
or path operations and imports.

💡 Key points:
    1️⃣ the basic syntax for problem5
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem5 affects the result.
"""

# Read one file and write its content to another. Handle errors such as
# a missing file or denied permission.
try:
    file = input("Enter a file name ")
    with open(file, "r") as f:
        data = f.read()
    copy_file = input("Choose your copy file name : ")
    with open(copy_file, "w") as f:
        f.write(data)
except FileNotFoundError:
    print("File is not available yet.")

except PermissionError:
    print("You can not handle this tasks.")
