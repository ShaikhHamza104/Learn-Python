# 🐍 Chapter 1 - Python Basics & Exercises

Welcome to **Chapter 1 Practice Exercises**! 🚀  
This guide will walk you through your very first Python programs step by step. Everything here is written simply so you can follow along easily even if you're a complete beginner.

---

## 📌 Exercises Overview

| File | Topic | Key Concept | Difficulty |
| :--- | :--- | :--- | :--- |
| 📄 [`problem1.py`](./problem1.py) | Twinkle Twinkle Little Star | Triple quotes (`'''`) for multi-line text | 🟢 Beginner |
| 🔢 [`problem2.py`](./problem2.py) | Table of 5 | Basic arithmetic and math operations in `print()` | 🟢 Beginner |
| 🔊 [`problem3.py`](./problem3.py) | Text to Speech | Installing & using external modules (`pyttsx3`) | 🟡 Easy - Medium |
| 📁 [`problem4.py`](./problem4.py) | List Directory Contents | Built-in `os` module (`os.listdir`) | 🟢 Beginner |
| 📝 [`problem5.py`](./problem5.py) | Documented Directory Explorer | Adding helpful comments to code | 🟢 Beginner |

---

## 🎭 Problem 1: Multi-line Printing (`problem1.py`)

### ❓ Question
> Write a program to print the *Twinkle Twinkle Little Star* poem in Python.

### 💻 Code
```python
print("""Twinkle, twinkle, little star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
...""")
```

### 💡 Key Takeaway
- Regular single quotes (`'`) or double quotes (`"`) only work for a single line of text.
- If you want text to span across multiple lines exactly as formatted, wrap it inside **triple quotes** (`"""` or `'''`).

▶️ **Run it:**
```bash
python problem1.py
```

---

## 🔢 Problem 2: Multiplication Table (`problem2.py`)

### ❓ Question
> Use REPL or write a Python program to print the multiplication table of 5.

### 💻 Code
```python
# Printing the table of 5 using basic print statements and arithmetic
print("5 x 1 =", 5 * 1)
print("5 x 2 =", 5 * 2)
print("5 x 3 =", 5 * 3)
print("5 x 4 =", 5 * 4)
print("5 x 5 =", 5 * 5)
print("5 x 6 =", 5 * 6)
print("5 x 7 =", 5 * 7)
print("5 x 8 =", 5 * 8)
print("5 x 9 =", 5 * 9)
print("5 x 10 =", 5 * 10)
```

### 💡 Key Takeaway
- Python can work as a calculator! You can do math operations like multiplication directly using the `*` symbol.
- Passing multiple arguments to `print()` separated by commas prints them with spaces in between.

▶️ **Run it:**
```bash
python problem2.py
```

---

## 🔊 Problem 3: Using External Modules (`problem3.py`)

### ❓ Question
> Install an external module and use it to perform an operation of your interest.

### 💻 Code
```python
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Tell Python what to say
engine.say("Hi i am good")

# Run the voice engine
engine.runAndWait()
```

### 📦 Installation
Before running this script, you must install the external package using `pip`:
```bash
pip install pyttsx3
```

### 💡 Key Takeaway
- **Modules** are pre-written libraries of code.
- **Built-in modules** (like `os`) come pre-installed with Python.
- **External modules** (like `pyttsx3`) need to be installed via `pip install <module-name>` before you can `import` them into your script.

▶️ **Run it:**
```bash
python problem3.py
```

---

## 📁 Problem 4: Listing Directory Contents (`problem4.py`)

### ❓ Question
> Write a Python program to print the contents of a directory using the `os` module.

### 💻 Code
```python
import os

# Define directory path ("/" means root directory)
directory_path = "/"

# Fetch list of files and folders inside directory_path
contents = os.listdir(directory_path)

# Loop through each item and print its name
for item in contents:
    print(item)
```

### 💡 Key Takeaway
- `import os`: Imports Python's standard operating system interface module.
- `os.listdir(path)`: Returns a list containing the names of the entries in the given directory.
- `for item in contents:`: A basic `for` loop that iterates over each file/folder and prints it.

▶️ **Run it:**
```bash
python problem4.py
```

---

## 📝 Problem 5: Clean Code with Comments (`problem5.py`)

### ❓ Question
> Write a Python program to print the contents of a directory using the `os` module, with comments explaining each step.

### 💻 Code
```python
import os

# Replace '/' with any folder path you want to explore (e.g. 'C:/' on Windows or '.' for current directory)
directory_path = "/"

# List the contents of the directory
contents = os.listdir(directory_path)

# Print each item in the directory one by one
for item in contents:
    print(item)
```

### 💡 Key Takeaway
- `#`: Single-line comments start with a hash symbol. Comments are ignored by Python when running the code.
- Writing clear comments helps other people (and future you!) understand what your code is doing and why.

▶️ **Run it:**
```bash
python problem5.py
```

---

## 🎯 Quick Recap

- 🔤 **Triple quotes (`"""`)**: Great for printing multi-line text and poems.
- 🔢 **Basic Math**: Python calculates math operations directly (`5 * 1`).
- 📦 **Pip & Modules**: `pip` installs third-party tools; `import` brings them into your code.
- 📂 **OS Module**: Allows your code to talk to your file system (`os.listdir`).
- ✍️ **Comments (`#`)**: Make your code easy to read and understand.

Happy Coding! 💻🎉
