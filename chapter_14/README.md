# 🐍 Chapter 14 — OS Module & Pathlib: File System Operations 🖥️

Welcome to Chapter 14! Python gives you direct access to the underlying operating system through the built-in `os` and `os.path` modules, as well as modern object-oriented paths via `pathlib`. This chapter covers directory traversal, folder creation and deletion, path validations, file metadata extraction, environment variables, system commands, and modern path manipulations.

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_getcwd.py` | Working Directory | `os.getcwd()` returns current directory |
| 02 | `02_chdir.py` | Change Directory | `os.chdir("../")` moves to another folder |
| 03 | `03_listdir.py` | Listing Directory | `os.listdir(".")` returns files and subfolders |
| 04 | `04_mkdir.py` | Single Directory Creation | `os.mkdir("new_folder")` |
| 05 | `05_makedirs.py` | Nested Directory Creation | `os.makedirs("a/b/c", exist_ok=True)` |
| 06 | `06_rmdir.py` | Remove Empty Directory | `os.rmdir("folder_name")` |
| 07 | `07_removedirs.py` | Remove Nested Directories | `os.removedirs("a/b/c")` |
| 08 | `08_rename.py` | Rename File or Folder | `os.rename("old.txt", "new.txt")` |
| 09 | `09_remove.py` | Delete a File | `os.remove("obsolete.txt")` |
| 10 | `10_path_exists.py` | Check Existence | `os.path.exists("target")` |
| 11 | `11_isfile.py` | Check if File | `os.path.isfile("data.csv")` |
| 12 | `12_isdir.py` | Check if Directory | `os.path.isdir("my_folder")` |
| 13 | `13_dirname.py` | Directory Name Extraction | `os.path.dirname("/a/b/file.txt")` |
| 14 | `14_getsize.py` | File Size | `os.path.getsize("file.txt")` in bytes |
| 15 | `15_getmtime.py` | Modification Timestamp | `os.path.getmtime("file.txt")` |
| 16 | `16_environ.py` | Environment Variables | `os.environ.get("PATH")` |
| 17 | `17_system.py` | Execute Shell Commands | `os.system("echo Hello from Shell")` |
| 18 | `18_pathlib_paths.py` | Modern Paths (`pathlib`) | `Path.cwd()`, `/` operator, `.rglob()` |

---

## 🗂️ 1. Directory Navigation & Modification (`01_getcwd.py` – `07_removedirs.py`)

```python
import os

# Where are we?
current_folder = os.getcwd()
print("Current folder:", current_folder)

# Create nested folders safely
os.makedirs("backup/daily/logs", exist_ok=True)

# List all items inside current directory
files_and_folders = os.listdir(".")
print("Contents:", files_and_folders)
```

---

## 🔎 2. Path Validations & Metadata (`10_path_exists.py` – `15_getmtime.py`)

```python
import os
import time

target = "sample.txt"

if os.path.exists(target):
    if os.path.isfile(target):
        size = os.path.getsize(target)
        mod_time = os.path.getmtime(target)
        readable_time = time.ctime(mod_time)
        print(f"File: {target} | Size: {size} bytes | Modified: {readable_time}")
    elif os.path.isdir(target):
        print(f"{target} is a directory.")
```

---

## 🌍 3. Environment Variables & System Shell (`16_environ.py`, `17_system.py`)

```python
import os

# Accessing environment variables
user_home = os.environ.get("USERPROFILE", os.environ.get("HOME"))
print("User Home:", user_home)

# Running shell commands (returns exit code)
exit_code = os.system("echo System shell connected!")
```

---

## 🚀 4. Modern `pathlib` vs `os.path` (`18_pathlib_paths.py`)

`pathlib` is the modern, object-oriented replacement for legacy string-based path operations:

```python
from pathlib import Path

# Finding all Python files recursively
current_dir = Path(".")
py_files = list(current_dir.rglob("*.py"))
for p in py_files:
    print(p.resolve())
```

---

## 🏋️ Practice Exercises
Check out **[chapter_14_exercises/](../chapter_14_exercises/README.md)** for 5 hands-on file system challenges!

---

## ⏭️ What's Next?
Next, discover how to extract and validate text patterns with **[Chapter 15 — Regular Expressions](../chapter_15_regex/README.md)**!
