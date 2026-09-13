# 🐍 Chapter 09 — File Handling & Enums: Persistent Data & Defined Constants 📁

Welcome to Chapter 9! Programs that store data only in variables lose everything when they exit. **File Handling** allows your programs to persist data across runs by reading from and writing to files. Additionally, this chapter covers modern file path operations using `pathlib`, working with structured formats (CSV & JSON), and creating type-safe named constants with Python's `enum` module.

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_file.py` | Introduction to File I/O | Basic `open()`, `.read()`, and `.close()` |
| 02 | `02_file_read_mode.py` | Reading Files (`"r"`) | `.readline()`, `.readlines()`, chunk reading |
| 03 | `03_file_write_mode.py` | Writing Files (`"w"`) | Creating and overwriting files with `.write()` |
| 04 | `04_file_append_mode.py` | Appending Files (`"a"`) | Adding new content to the end without deleting |
| 05 | `05_file_x_mode.py` | Exclusive Creation (`"x"`) | Fails safely if the file already exists (`FileExistsError`) |
| 06 | `06_with_statement.py` | The `with` Statement | Context managers for automatic file closing |
| 07 | `07_csv_read_write.py` | CSV Processing | Using the standard `csv` module for tabular data |
| 08 | `08_json_read_write.py` | JSON Serialization | Working with `json.dump()` and `json.load()` |
| 09 | `09_pathlib_basics.py` | Modern Paths (`pathlib`) | Object-oriented paths using `Path` |
| 10 | `10_enum.py` | Enumerations (`enum`) | Symbolic constants with `Enum`, `auto()`, and `@unique` |

---

## 📄 1. File Modes & Context Managers (`01_file.py` – `06_with_statement.py`)

Python provides different modes to open files:

| Mode | Name | Description |
|---|---|---|
| `"r"` | Read | Default mode. Opens a file for reading; errors if file doesn't exist. |
| `"w"` | Write | Opens for writing. Creates file if missing; **truncates/overwrites** if it exists. |
| `"a"` | Append | Opens for writing. Adds data to the end without truncating. |
| `"x"` | Exclusive | Creates a new file. Fails with `FileExistsError` if the file exists. |
| `"t"` / `"b"` | Text / Binary | Text mode (default) vs. binary mode (images, executables). |

### The Golden Standard: `with` Statement
Always use the `with` statement because it guarantees that the file is closed properly even if an error occurs:

```python
# Writing
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Hello from Python!\nLine 2.")

# Reading
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

---

## 📊 2. Working with CSV & JSON (`07_csv_read_write.py`, `08_json_read_write.py`)

### CSV (Comma Separated Values):
```python
import csv

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])
    writer.writerow(["Hamza", 95])
```

### JSON (JavaScript Object Notation):
```python
import json

data = {"user": "hamza", "role": "admin", "skills": ["Python", "Git"]}

# Serializing to file
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

# Deserializing from file
with open("user.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
```

---

## 🗂️ 3. Modern Paths with `pathlib` (`09_pathlib_basics.py`)

`pathlib` replaces clumsy string concatenations with intuitive object-oriented methods:

```python
from pathlib import Path

# Current directory and building subpaths
base_dir = Path.cwd()
config_file = base_dir / "data" / "config.json"

print("Exists:", config_file.exists())
print("File name:", config_file.name)
print("File extension:", config_file.suffix)
```

---

## 🏷️ 4. Python Enumerations (`10_enum.py`)

Enums provide type-safe, human-readable symbolic constants:

```python
from enum import Enum, auto, unique

@unique
class Status(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()

current_status = Status.PENDING
print(current_status.name)   # "PENDING"
print(current_status.value)  # 1
```

---

## 🏋️ Practice Exercises
Put file reading, log analysis, and replacement algorithms to work across 11 practice problems in **[chapter_09_exercises/](../chapter_09_exercises/README.md)**!

---

## ⏭️ What's Next?
Step into the world of **Object-Oriented Programming (OOP)** in **[Chapter 10 — OOP](../chapter_10/README.md)**!
