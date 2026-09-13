# 🐍 Chapter 12 Exercises — Exception Handling Practice 🛡️

Welcome to the **Chapter 12 Practice Exercises**! 🚀  
These 10 problems focus on real-world error recovery: preventing crashes when files are missing, handling mathematical anomalies (division by zero), cleanly accessing list elements with `enumerate()`, generating data via comprehensions, and saving outputs safely.

---

## 📌 Exercises Overview

| File | Topic | Core Concept | Difficulty |
|---|---|---|---|
| 📂 [`problem1.py`](./problem1.py) | Multi-File Missing Tolerant Reader | Catching `FileNotFoundError` without exiting | 🟢 Beginner |
| 🔢 [`problem2.py`](./problem2.py) | Selective Index Access | Filtering indices `[2, 4, 6]` with `enumerate()` | 🟢 Beginner |
| ⚡ [`problem3.py`](./problem3.py) | Table via List Comprehension | One-line generation `[n * i for i in range(1, 11)]` | 🟢 Beginner |
| ♾️ [`problem4.py`](./problem4.py) | Safe Division / Handle Zero | Catching `ZeroDivisionError` -> "Infinite" | 🟢 Beginner |
| 💾 [`problem5.py`](./problem5.py) | Persist Generated Tables | Writing comprehension results to `Tables.txt` | 🟢 Beginner |
| 🛡️ [`problem6.py`](./problem6.py) – [`problem10.py`](./problem10.py) | Advanced Exception Patterns | `IndexError`, custom exceptions, logging tracebacks | 🟡 Easy-Medium |

---

## 📂 Problem 1: Non-Crashing Multi-File Reader (`problem1.py`)

### ❓ Objective
Write a program to open three files (`1.txt`, `2.txt`, `3.txt`). If any of these files are not present, print a friendly message without terminating the program.

### 💻 Code
```python
files = ["1.txt", "2.txt", "3.txt"]

for filename in files:
    try:
        with open(filename, "r") as f:
            print(f"Content of {filename}:\n{f.read()}")
    except FileNotFoundError:
        print(f"⚠️ Notice: '{filename}' was not found.")
```

▶️ **Run:** `python problem1.py`

---

## 🔢 Problem 2: 3rd, 5th, and 7th Elements (`problem2.py`)

### ❓ Objective
Write a program to print the 3rd, 5th, and 7th element from a list using the `enumerate()` function.

### 💻 Code
```python
items = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

for index, value in enumerate(items):
    # 3rd is index 2, 5th is index 4, 7th is index 6
    if index in (2, 4, 6):
        print(f"Index {index} (Position {index + 1}): {value}")
```

▶️ **Run:** `python problem2.py`

---

## ⚡ Problem 3: Table via List Comprehension (`problem3.py`)

### ❓ Objective
Write a list comprehension to generate the multiplication table of a user-entered number.

### 💻 Code
```python
n = int(input("Enter number: "))
table = [n * i for i in range(1, 11)]
print("Multiplication Table:", table)
```

▶️ **Run:** `python problem3.py`

---

## ♾️ Problem 4: Safe Division (`problem4.py`)

### ❓ Objective
Write a program to display `a / b` where `a` and `b` are integers. If `b == 0`, display "Infinite" by catching `ZeroDivisionError`.

### 💻 Code
```python
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = a / b
    print(f"{a} / {b} = {result}")
except ZeroDivisionError:
    print(f"{a} / {b} = Infinite")
except ValueError:
    print("Please enter valid integers!")
```

▶️ **Run:** `python problem4.py`

---

## 💾 Problem 5: Persist Table to File (`problem5.py`)

### ❓ Objective
Store the multiplication tables generated in Problem 3 inside a file named `Tables.txt`.

### 💻 Code
```python
n = int(input("Enter number: "))
table = [f"{n} x {i} = {n * i}\n" for i in range(1, 11)]

with open("Tables.txt", "a", encoding="utf-8") as f:
    f.writelines(table)
    f.write("-" * 20 + "\n")

print(f"Table for {n} saved to Tables.txt!")
```

▶️ **Run:** `python problem5.py`

---

## ⏭️ What's Next?
Next, discover how to architect modular projects and reusable packages in **[Chapter 13 — Modules & Packages](../chapter_13/README.md)**!
