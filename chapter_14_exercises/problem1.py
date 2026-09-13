"""
📚 Topic: Problem 1 - Current Directory & Listing (Easy)

This script demonstrates directory listing using the os module, functions,
and exception handling.

💡 Key points:
1️⃣ the basic syntax for os.getcwd() and os.listdir()
2️⃣ how os modules interact with your local file system
3️⃣ what to look for when you check the returned list of files

🧠 Beginner tip:
Run this file in different folders on your computer to see how the output
changes based on your current working directory.
"""

import os

# 1. Write a program that gets the current working directory and lists all
# files and folders inside it.


def get_current_directory():
    try:
        current_directory = os.getcwd()
        print("Current directory:", current_directory)
        files = os.listdir(current_directory)
        print("Files in current directory:", files)
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Input cancelled")
    except Exception as e:
        print("Error:", e)


get_current_directory()
