"""
📚 Topic: Problem 3 - Path Validation (Medium)

This script demonstrates path checking using os.path, functions, and
exception handling.

💡 Key points:
1️⃣ the difference between os.path.isfile() and os.path.isdir()
2️⃣ how to check if a path exists at all using os.path.exists()
3️⃣ what to look for when you input relative vs. absolute paths

🧠 Beginner tip:
Try inputting the name of this python script, then try inputting the name
of the folder it sits inside to see the different conditional outputs.
"""

import os

# 3. Write a program that takes a file or folder path as input and tells
# the user whether it exists, and specifically if it is a file or a directory.


def validate_path():
    try:
        path = input("Enter a file or folder path: ")
        if os.path.exists(path):
            if os.path.isfile(path):
                print("Path exists and it is a file")
            elif os.path.isdir(path):
                print("Path exists and it is a directory")
        else:
            print("Path does not exist")
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Input cancelled")
    except Exception as e:
        print("Error:", e)


validate_path()
