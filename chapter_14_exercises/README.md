# 🐍 Chapter 14 Exercises — OS Module & Pathlib Practice 🖥️

Welcome to the **Chapter 14 Practice Exercises**! 🚀  
These 5 exercises guide you through real-world system tasks: inspecting directories, safely handling filesystem collisions, validating paths, extracting file size and modification timestamps, and recursively discovering files with `pathlib`.

---

## 📌 Exercises Overview

| File | Topic | Core Concept | Difficulty |
|---|---|---|---|
| 📂 [`problem1.py`](./problem1.py) | Working Directory & Listing | `os.getcwd()` and `os.listdir()` | 🟢 Beginner |
| 📁 [`problem2.py`](./problem2.py) | Safe Directory Creation | `os.mkdir()` with `FileExistsError` handling | 🟡 Easy-Medium |
| 🔍 [`problem3.py`](./problem3.py) | Path Type Validation | `os.path.exists()`, `.isfile()`, `.isdir()` | 🟡 Easy-Medium |
| 📊 [`problem4.py`](./problem4.py) | File Metadata & Timestamp | `os.path.getsize()`, `getmtime()`, `time.ctime()` | 🟡 Easy-Medium |
| 🚀 [`problem5.py`](./problem5.py) | Recursive Search with `pathlib` | `Path.rglob("*.py")` and `.resolve()` | 🔴 Medium |

---

## 📂 Problem 1: Current Directory Explorer (`problem1.py`)

### ❓ Objective
Write a program that gets the current working directory and lists all files and folders inside it.

### 💻 Code
```python
import os

def get_current_directory():
    try:
        current_directory = os.getcwd()
        print("Current directory:", current_directory)
        files = os.listdir(current_directory)
        print("Files in current directory:", files)
    except Exception as e:
        print("Error:", e)

get_current_directory()
```

▶️ **Run:** `python problem1.py`

---

## 📁 Problem 2: Safe Folder Creation (`problem2.py`)

### ❓ Objective
Write a program that asks the user for a folder name and creates it in the current directory, handling the error cleanly if it already exists.

### 💻 Code
```python
import os

def create_directory():
    try:
        folder_name = input("Enter the folder name to create: ").strip()
        os.mkdir(folder_name)
        print(f"Directory '{folder_name}' created successfully!")
    except FileExistsError:
        print(f"Error: A directory or file named '{folder_name}' already exists.")
    except Exception as e:
        print("An error occurred:", e)

create_directory()
```

▶️ **Run:** `python problem2.py`

---

## 🔍 Problem 3: Path Existence and Type Validation (`problem3.py`)

### ❓ Objective
Write a program that takes a file or folder path as input and tells the user whether it exists, and specifically if it is a file or a directory.

### 💻 Code
```python
import os

def validate_path():
    path = input("Enter a file or folder path: ").strip()
    if os.path.exists(path):
        if os.path.isfile(path):
            print(f"'{path}' is an existing regular file.")
        elif os.path.isdir(path):
            print(f"'{path}' is an existing directory.")
    else:
        print(f"'{path}' does NOT exist!")

validate_path()
```

▶️ **Run:** `python problem3.py`

---

## 📊 Problem 4: File Size & Modification Timestamp (`problem4.py`)

### ❓ Objective
Write a program that takes a file path as input and prints its size in bytes and its last modification date in human-readable format.

### 💻 Code
```python
import os
import time

def get_file_metadata():
    path = input("Enter file path: ").strip()
    if os.path.exists(path) and os.path.isfile(path):
        size = os.path.getsize(path)
        mtime = os.path.getmtime(path)
        readable_time = time.ctime(mtime)
        print(f"File Size: {size} bytes")
        print(f"Last Modified: {readable_time}")
    else:
        print("Path does not exist or is not a regular file.")

get_file_metadata()
```

▶️ **Run:** `python problem4.py`

---

## 🚀 Problem 5: Modern Recursive Search with `pathlib` (`problem5.py`)

### ❓ Objective
Write a program using `pathlib` that searches the current directory and all subdirectories for any Python (`.py`) files, printing their absolute paths.

### 💻 Code
```python
from pathlib import Path

def find_py_files():
    current_path = Path(".")
    py_files = list(current_path.rglob("*.py"))
    if py_files:
        print(f"Found {len(py_files)} Python files:")
        for file in py_files:
            print(" -", file.resolve())
    else:
        print("No Python files found.")

find_py_files()
```

▶️ **Run:** `python problem5.py`

---

## ⏭️ What's Next?
Now learn pattern matching and text parsing with **[Chapter 15 — Regular Expressions](../chapter_15_regex/README.md)**!
