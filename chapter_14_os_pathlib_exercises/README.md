# 📚 Topic: OS Module & Pathlib Practice (Exercises)

This folder contains 5 hands-on practice problems exercising file system manipulation, directory management, and modern path traversal in Python. The exercises build confidence in using both the classic `os` / `os.path` modules and the modern `pathlib.Path` library.

---

## 📂 What's in this folder

| File | Description |
| --- | --- |
| `problem1.py` | Querying the current working directory and listing files with `os.getcwd()` and `os.listdir()` |
| `problem2.py` | Safely creating user-specified directories using `os.mkdir()` with `FileExistsError` handling |
| `problem3.py` | Validating user-provided paths and distinguishing files from directories using `os.path` |
| `problem4.py` | Inspecting file metadata including byte size and human-readable modification timestamps |
| `problem5.py` | Recursively searching nested directory trees for `.py` files using `pathlib.Path.rglob()` |

---

## 💡 Key points

1. **Current Directory Inspection (`problem1.py`)**: `os.getcwd()` retrieves the active process folder, while `os.listdir()` enumerates all child files and directories inside it.
2. **Defensive Directory Creation (`problem2.py`)**: Requesting a directory name and wrapping `os.mkdir(folder_name)` in `try-except FileExistsError` prevents crashes when duplicate folders are requested.
3. **Path Type Verification (`problem3.py`)**: Combining `os.path.exists()` with `os.path.isfile()` and `os.path.isdir()` cleanly branches logic based on filesystem entity types.
4. **File Metadata & Time Formatting (`problem4.py`)**: `os.path.getsize()` retrieves file size in bytes, and `os.path.getmtime()` retrieves last modification epoch seconds converted to readable timestamps with `time.ctime()`.
5. **Modern Recursive Discovery (`problem5.py`)**: The `pathlib.Path.rglob("*.py")` generator discovers all matching files across arbitrary directory depth, while `.resolve()` returns clean absolute paths.

---

## 🧠 Beginner tip

When taking file paths as user input or handling paths across operating systems, remember that Windows paths use backslashes (`\`) while Unix paths use forward slashes (`/`). Passing raw string inputs directly to `Path(user_input)` normalizes path separators automatically, eliminating cross-platform path-handling bugs.

---

## 📊 Where this is used in Data Science

- **Batch Dataset Discovery**: Data ingestion pipelines use `Path.rglob("*.csv")` or `*.parquet` to scan nested monthly/daily raw data folders across data lakes without hardcoding path structures.
- **Model Checkpoint Auditing**: Automated evaluation scripts inspect model directories using `os.path.getmtime()` and `os.path.getsize()` to locate the most recently saved checkpoint weights and verify they are non-empty before running inference.
- **Dynamic Artifact Output**: Machine learning pipelines generate unique experiment run directories using guarded directory creation to prevent overwriting prior model runs or logs.

---

## 🏃 How to Run Each Exercise

Run each problem file directly using Python:

```bash
# Problem 1: Inspect working directory and list contents
python problem1.py

# Problem 2: Safely create a directory with collision handling
python problem2.py

# Problem 3: Validate existence and check file vs directory
python problem3.py

# Problem 4: Read file size and modification timestamp
python problem4.py

# Problem 5: Search directory recursively for Python files using pathlib
python problem5.py
```

---

## 📖 Related Lessons

Review directory management and `pathlib` foundations in **[Chapter 14 — OS Module & Pathlib](../chapter_14_os_pathlib/README.md)**.

---

## ⏭️ What's Next

Learn text parsing, regex syntax, and pattern matching in **[Chapter 15 — Regular Expressions](../chapter_15_regex/README.md)**!
