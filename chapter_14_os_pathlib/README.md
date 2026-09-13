# 📚 Topic: OS Module & Pathlib

Interacting with the file system and operating system is essential for real-world software. Python provides low-level operating system interfaces via the `os` and `os.path` modules, alongside the modern, object-oriented `pathlib` library. This chapter covers navigating directories, creating and deleting folder trees, querying file metadata, executing subshell commands, and writing cross-platform path logic.

---

## 📂 What's in this folder

| File | What it teaches |
| --- | --- |
| `01_getcwd.py` | Retrieving the current working directory with `os.getcwd()` |
| `02_chdir.py` | Changing the active working directory with `os.chdir()` |
| `03_listdir.py` | Listing files and subdirectories in a directory with `os.listdir()` |
| `04_mkdir.py` | Creating a single directory with `os.mkdir()` and handling `FileExistsError` |
| `05_makedirs.py` | Creating nested multi-level directory trees with `os.makedirs()` |
| `06_rmdir.py` | Removing an empty directory with `os.rmdir()` and catching `OSError` if not empty |
| `07_removedirs.py` | Removing empty directory hierarchies recursively with `os.removedirs()` |
| `08_rename.py` | Renaming and moving files or directories with `os.rename()` and handling type errors |
| `09_remove.py` | Deleting files with `os.remove()` and handling `PermissionError` |
| `10_path_exists.py` | Verifying path existence using `os.path.exists()` |
| `11_isfile.py` | Checking whether a path points to an existing file with `os.path.isfile()` |
| `12_isdir.py` | Checking whether a path points to an existing directory with `os.path.isdir()` |
| `13_dirname.py` | Extracting the directory component of a path string with `os.path.dirname()` |
| `14_getsize.py` | Reading file size in bytes using `os.path.getsize()` |
| `15_getmtime.py` | Retrieving last modification timestamps using `os.path.getmtime()` |
| `16_environ.py` | Reading operating system environment variables (such as `PATH`) with `os.environ` |
| `17_system.py` | Executing terminal commands in a subshell using `os.system()` |
| `18_pathlib_paths.py` | Modern object-oriented path handling with `pathlib.Path` (`/` operator, `.mkdir(exist_ok=True)`, `.unlink()`, `.iterdir()`) |

---

## 💡 Key points

1. **Current Working Directory (`01_getcwd.py`)**: `os.getcwd()` returns an absolute string path representing the folder where Python was invoked.
2. **Directory Navigation (`02_chdir.py`)**: `os.chdir(path)` alters the active working directory for the current process, affecting subsequent relative path resolutions.
3. **Directory Listing (`03_listdir.py`)**: `os.listdir(path)` returns a list of filename strings present inside the target directory.
4. **Single Directory Creation (`04_mkdir.py`)**: `os.mkdir(path)` creates a single directory level, raising `FileExistsError` if the folder already exists.
5. **Recursive Directory Creation (`05_makedirs.py`)**: `os.makedirs(path)` creates all intermediate parent directories required to satisfy the full nested path.
6. **Directory Deletion (`06_rmdir.py`)**: `os.rmdir(path)` deletes an empty directory; attempting to remove a non-empty directory raises `OSError`.
7. **Recursive Directory Deletion (`07_removedirs.py`)**: `os.removedirs(path)` removes empty leaf directories and traverses backwards removing parent directories until a non-empty folder is reached.
8. **Path Renaming & Moving (`08_rename.py`)**: `os.rename(src, dst)` renames or moves a filesystem item, requiring careful handling of `IsADirectoryError`, `NotADirectoryError`, and `PermissionError`.
9. **File Deletion (`09_remove.py`)**: `os.remove(file_path)` deletes a specific file permanently from disk, guarded by `PermissionError` and `FileNotFoundError`.
10. **Path Validation (`10_path_exists.py`)**: `os.path.exists(path)` evaluates whether any file or directory exists at the given string path.
11. **Type Inspection (`11_isfile.py`, `12_isdir.py`)**: `os.path.isfile(path)` and `os.path.isdir(path)` verify whether an existing path is a regular file or a directory container.
12. **Metadata & Inspection (`13_dirname.py`, `14_getsize.py`, `15_getmtime.py`)**: `os.path.dirname()` returns the parent path string, `os.path.getsize()` returns file size in bytes, and `os.path.getmtime()` returns epoch seconds of the last modification.
13. **Environment & System Shells (`16_environ.py`, `17_system.py`)**: `os.environ` provides dictionary-like access to system environment variables, while `os.system()` runs terminal commands in a subshell and returns their exit code.
14. **The Modern `pathlib` Standard (`18_pathlib_paths.py`)**: The `pathlib.Path` class provides an object-oriented API where paths are constructed cleanly with `/` (`Path("data") / "file.csv"`), created safely with `.mkdir(exist_ok=True)`, iterated via `.iterdir()`, and deleted with `.unlink()`.

---

## 🧠 Beginner tip

Prefer `pathlib.Path` over legacy `os` and `os.path` functions for new code. `pathlib` eliminates slash mismatches between Windows (`\`) and Unix (`/`) by allowing path joins with the `/` operator (e.g., `Path("data") / "raw" / "dataset.csv"`). When creating folders, pass `exist_ok=True` to `.mkdir()` (or `os.makedirs()`) to prevent `FileExistsError` if the directory is already created.

---

## 📊 Where this is used in Data Science

- **Automated Dataset Scanners**: Data processing jobs use `Path.iterdir()` or `.rglob("*.parquet")` to discover, batch-load, and aggregate thousands of telemetry or sensor files distributed across subdirectories.
- **Model Checkpoint Management**: Deep learning frameworks (PyTorch, TensorFlow) use `Path.mkdir(parents=True, exist_ok=True)` to create structured timestamped directories (`models/checkpoints/run_01/`) before saving model weights and evaluation graphs.
- **Environment & Credentials Loading**: Training pipelines read cloud credentials, API keys, and data bucket paths from `os.environ` (e.g., `AWS_ACCESS_KEY_ID`, `GCS_BUCKET_NAME`) rather than hardcoding secret paths.

---

## 🛠️ Code Examples

### Legacy `os` vs Modern `pathlib`
```python
import os
from pathlib import Path

# Legacy os module
folder = "exports"
if not os.path.exists(folder):
    os.mkdir(folder)
legacy_file = os.path.join(folder, "report.csv")

# Modern pathlib
export_dir = Path("exports")
export_dir.mkdir(exist_ok=True)
modern_file = export_dir / "report.csv"
```

### Iterating and Filtering Files with `pathlib`
```python
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Scan for all CSV files in directory
for csv_file in data_dir.glob("*.csv"):
    print(f"Processing {csv_file.name}, size: {csv_file.stat().st_size} bytes")
```

### Reading Environment Variables Safely
```python
import os

# os.environ.get provides a default fallback if variable is unset
database_url = os.environ.get("DATABASE_URL", "sqlite:///local.db")
print("Connecting to:", database_url)
```

---

## 🏋️ Practice Exercises

Apply your file system management skills with hands-on exercises in **[chapter_14_os_pathlib_exercises/](../chapter_14_os_pathlib_exercises/README.md)**!

---

## ⏭️ What's Next

Master text searching, pattern matching, and input validation using **[Chapter 15 — Regular Expressions](../chapter_15_regex/README.md)**!
