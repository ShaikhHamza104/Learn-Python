# 🐍 Chapter 09 Exercises — File Handling Practice 📁

Welcome to the **Chapter 09 Practice Exercises**! 🚀  
These 11 problems cover text searching, high-score tracking, bulk table generation, word censorship, log mining, file copying, identity verification, file wiping, and file renaming.

---

## 📌 Exercises Overview

| File | Topic | Core Concept | Difficulty |
|---|---|---|---|
| 📜 [`problem1.py`](./problem1.py) | Search Word in Poem | `.read()` and membership check (`"twinkle" in text`) | 🟢 Beginner |
| 🎮 [`problem2.py`](./problem2.py) | High-Score Manager | Reading previous score, comparing, and overwriting | 🟡 Easy-Medium |
| ✖️ [`problem3.py`](./problem3.py) | Bulk Table Generator | Generating 19 files (`table_2.txt` to `table_20.txt`) | 🟡 Easy-Medium |
| 🚫 [`problem4.py`](./problem4.py) | Single Word Censorship | Reading, `.replace("Donkey", "######")`, writing back | 🟢 Beginner |
| 🤬 [`problem5.py`](./problem5.py) | Multi-Word Profanity Filter | Looping through a blacklist and replacing words | 🟡 Easy-Medium |
| ⛏️ [`problem6.py`](./problem6.py) | Log File Mining | Searching for "python" in server logs | 🟢 Beginner |
| 📍 [`problem7.py`](./problem7.py) | Line Number Identification | Iterating with `enumerate(f)` to locate matching line | 🟡 Easy-Medium |
| 📋 [`problem8.py`](./problem8.py) | Duplicate / Copy File | Reading source file and writing into target file | 🟢 Beginner |
| ⚖️ [`problem9.py`](./problem9.py) | Compare Two Files | Verifying if two files have identical byte/text contents | 🟢 Beginner |
| 🧹 [`problem10.py`](./problem10.py) | Wipe File Contents | Opening with mode `"w"` without writing content | 🟢 Beginner |
| 🏷️ [`problem11.py`](./problem11.py) | Rename File | Renaming with `os.rename()` / `Path.rename()` | 🟢 Beginner |

---

## 📜 Problem 1: Word Presence in Poems (`problem1.py`)

### 💻 Code
```python
with open("poems.txt", "r", encoding="utf-8") as f:
    content = f.read()

if "twinkle" in content.lower():
    print("'twinkle' is present in the poem.")
else:
    print("'twinkle' was not found.")
```

▶️ **Run:** `python problem1.py`

---

## 🎮 Problem 2: High Score Updater (`problem2.py`)

### 💻 Code
```python
def game():
    return 85  # Current game score

score = game()

try:
    with open("Hi-score.txt", "r") as f:
        hi_score = int(f.read().strip())
except (FileNotFoundError, ValueError):
    hi_score = 0

if score > hi_score:
    with open("Hi-score.txt", "w") as f:
        f.write(str(score))
    print(f"🎉 New High Score: {score}!")
else:
    print(f"Score: {score}. High score remains {hi_score}.")
```

▶️ **Run:** `python problem2.py`

---

## ✖️ Problem 3: 2 to 20 Multiplication Tables Files (`problem3.py`)

### 💻 Code
```python
from pathlib import Path

Path("tables").mkdir(exist_ok=True)

for n in range(2, 21):
    table_content = "".join(f"{n} x {i} = {n * i}\n" for i in range(1, 11))
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table_content)
```

▶️ **Run:** `python problem3.py`

---

## 🚫 Problems 4 & 5: Word Censorship Filters (`problem4.py`, `problem5.py`)

### 💻 Code
```python
words_to_censor = ["donkey", "badword", "spam"]

with open("content.txt", "r") as f:
    text = f.read()

for word in words_to_censor:
    text = text.replace(word, "#" * len(word))

with open("content.txt", "w") as f:
    f.write(text)
```

▶️ **Run:** `python problem4.py`

---

## 📍 Problems 6 & 7: Log Mining with Line Numbers (`problem6.py`, `problem7.py`)

### 💻 Code
```python
found = False

with open("log.txt", "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        if "python" in line.lower():
            print(f"Python found at line {line_num}: {line.strip()}")
            found = True

if not found:
    print("Python was not mentioned in the log.")
```

▶️ **Run:** `python problem7.py`

---

## 📋 Problems 8, 9, 10 & 11: File Utilities (`problem8.py` – `problem11.py`)

### Copy File (`problem8.py`):
```python
with open("this.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())
```

### Compare Files (`problem9.py`):
```python
with open("file1.txt") as f1, open("file2.txt") as f2:
    if f1.read() == f2.read():
        print("Files are identical!")
```

### Wipe File (`problem10.py`):
```python
with open("wipe_me.txt", "w") as f:
    pass  # Opening in 'w' mode instantly truncates file to 0 bytes
```

### Rename File (`problem11.py`):
```python
import os
os.rename("old_name.txt", "renamed_by_python.txt")
```

---

## ⏭️ What's Next?
Now step into **Object-Oriented Programming** in **[Chapter 10 — OOP](../chapter_10/README.md)**!
