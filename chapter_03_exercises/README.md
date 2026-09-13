# 🐍 Chapter 3 Exercises — Strings in Action 📜

Welcome to the **Chapter 3 Practice Exercises**! 🚀  
Here, you'll put your string-manipulation skills to work. You will practice string input, multi-line templates, search methods, string replacement, and escape sequences.

---

## 📌 Exercises Overview

| File | Topic | Key Concept | Difficulty |
| :--- | :--- | :--- | :--- |
| 🍎 [`problem1.py`](./problem1.py) | User Input & Lists | Collecting fruit names into a list | 🟢 Beginner |
| ✉️ [`problem2.py`](./problem2.py) | Letter Template | Multi-line string replacement with `.replace()` | 🟢 Beginner |
| 🔍 [`problem3.py`](./problem3.py) | Detect Double Spaces | Searching for substrings using `.find()` | 🟢 Beginner |
| ✂️ [`problem4.py`](./problem4.py) | Replace Double Spaces | Cleaning text with `.replace("  ", " ")` | 🟢 Beginner |
| 💬 [`problem5.py`](./problem5.py) | Escape Sequences | Formatting strings with `\t` and `\n` | 🟢 Beginner |

---

## 🍎 Problem 1: Collecting Strings (`problem1.py`)

### ❓ Objective
Write a program that takes names of 5 fruits from the user and stores them in a list.

### 💻 Code
```python
fruits = []

f1 = input("Enter Fruit name : ")
fruits.append(f1)
f2 = input("Enter Fruit name : ")
fruits.append(f2)
f3 = input("Enter Fruit name : ")
fruits.append(f3)
f4 = input("Enter Fruit name : ")
fruits.append(f4)
f5 = input("Enter Fruit name : ")
fruits.append(f5)

print("Fruits list:", fruits)
```

### 💡 Key Takeaway
- `input()` always returns text as a string (`str`).
- You can collect multiple string values sequentially and append them into a Python `list`.

▶️ **Run it:**
```bash
python problem1.py
```

---

## ✉️ Problem 2: Letter Template (`problem2.py`)

### ❓ Objective
Write a program to fill in a letter template with a given name and date using string replacement.

### 💻 Code
```python
letter = """
Dear <|Name|>,
You are selected!
<|Date|>
"""

name = "Hamza"
date = "09-05-2024"

print(letter.replace("<|Name|>", name).replace("<|Date|>", date))
```

### 💡 Key Takeaway
- Chaining `.replace()` allows multiple placeholders to be substituted one after another.
- Because strings are **immutable**, `.replace()` returns a brand new string and leaves the original untouched.

▶️ **Run it:**
```bash
python problem2.py
```

---

## 🔍 Problem 3: Detecting Double Spaces (`problem3.py`)

### ❓ Objective
Write a program to detect double spaces inside a string.

### 💻 Code
```python
string = "Python is programming language.Its easy to understand language  "

if string.find("  ") != -1:
    print("double space is detect")
```

### 💡 Key Takeaway
- `str.find(sub)` returns the lowest index where `sub` is found.
- If the substring is not present, `.find()` returns `-1`.

▶️ **Run it:**
```bash
python problem3.py
```

---

## ✂️ Problem 4: Removing Double Spaces (`problem4.py`)

### ❓ Objective
Write a program to replace double spaces in a string with a single space.

### 💻 Code
```python
string = "Python is programming language.Its easy  to understand language"
print(string.replace("  ", " "))
```

### 💡 Key Takeaway
- `.replace("  ", " ")` scans the string and substitutes all instances of two consecutive spaces with a single space.
- Useful for cleaning messy user inputs and text datasets.

▶️ **Run it:**
```bash
python problem4.py
```

---

## 💬 Problem 5: Formatting with Escape Sequences (`problem5.py`)

### ❓ Objective
Format a letter using escape sequences (`\t`, `\n`) to make it neat and readable.

### 💻 Code
```python
letter = "Dear Harry,\tthis python course is nice. Thanks!"
print(letter)
```

### 💡 Key Takeaway
- `\t` inserts a horizontal tab spacing.
- `\n` inserts a new line.
- Escape characters give you precise formatting control inside single-line string literals.

▶️ **Run it:**
```bash
python problem5.py
```

---

## 🎯 Quick Recap

| Concept | Syntax / Example | Purpose |
| :--- | :--- | :--- |
| **String Input** | `name = input("Enter: ")` | Read user text |
| **Substrings** | `text.find("sub")` | Returns index or `-1` |
| **Replacement** | `text.replace("old", "new")` | Replace matching segments |
| **Escape Codes** | `\n` (newline), `\t` (tab) | Format console output |

---

## ⏭️ What's Next?
Ready for collections of data? Head over to **[Chapter 04 — Lists & Tuples](../chapter_04/README.md)**!
