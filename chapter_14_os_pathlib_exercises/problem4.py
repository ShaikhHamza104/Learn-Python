"""
📚 Topic: Problem 4 - File Metadata (Medium-Advanced)

This script demonstrates retrieving file size and modification times using
os.path, time, functions, and exception handling.

💡 Key points:
1️⃣ the basic syntax for os.path.getsize() and os.path.getmtime()
2️⃣ how time.ctime() is used to convert raw timestamps into readable formats
3️⃣ what to look for when you check files of drastically different sizes

🧠 Beginner tip:
Find a large video file on your computer and paste its absolute path into
this script to see its size in bytes.
"""

import os
import time


# 4. Write a program that takes a file path as input and prints out its
# size in bytes and its last modification date in a human-readable format.


def get_file_metadata():
    try:
        file_path = input("Enter a file path: ")
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                mod_time = os.path.getmtime(file_path)
                print("File size:", file_size, "bytes")
                print("Last modification date:", time.ctime(mod_time))
            else:
                print("Path is a directory, not a file")
        else:
            print("Path does not exist")
    except ValueError:
        print("Invalid input")
    except KeyboardInterrupt:
        print("Input cancelled")
    except Exception as e:
        print("Error:", e)


get_file_metadata()
