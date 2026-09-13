"""
📚 Topic: Problem 2 - Safely Creating Directories (Easy-Medium)

This script demonstrates directory creation using os.mkdir, functions,
and exception handling.

💡 Key points:
1️⃣ the basic syntax for creating a new folder using os.mkdir()
2️⃣ how to handle FileExistsError when a folder already exists
3️⃣ what to look for in your file explorer after running the script

🧠 Beginner tip:
Run this file twice! The first time it will create the folder. The second
time, it will trigger the exception handling, showing you how safe code works.
"""

import os


# 2. Write a program that asks the user for a folder name and creates it
# in the current directory, handling the error if it already exists.


def create_directory():
    try:
        folder_name = input("Enter folder name: ")
        os.mkdir(folder_name)
        print("Folder created successfully")
    except FileExistsError:
        print("Folder already exists")
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Input cancelled")
    except Exception as e:
        print("Error:", e)


create_directory()
