# 📚 Topic: File Handling

File handling enables Python programs to persist data across execution sessions by reading from and writing to disk. This chapter covers standard file opening modes (`r`, `w`, `a`, `x`), reading methods (`read`, `readline`, `readlines`), context managers with `with`, tabular data handling with the `csv` module, serialization with `json`, object-oriented filesystem path management using `pathlib`, and creating type-safe enumeration constants with `enum`.

## 📂 What's in this folder

| File | What it teaches |
|---|---|
| `01_file.py` | Basic file I/O operations using `open()`, `.read()`, and manual stream closing with `.close()`. |
| `02_file_read_mode.py` | Text reading techniques comparing full file reading (`.read()`), single-line reads (`.readline()`), and list-based line reads (`.readlines()`). |
| `03_file_write_mode.py` | Overwriting and writing data to text files using `'w'` mode with `.write()` and `.writelines()`. |
| `04_file_append_mode.py` | Appending new lines to an existing file using `'a'` mode without erasing earlier content. |
| `05_file_x_mode.py` | Exclusive creation mode `'x'` to safely prevent overwriting files that already exist on disk. |
| `06_with_statement.py` | Clean context management using the `with` statement to guarantee automatic file closing. |
| `07_csv_read_write.py` | Reading and writing CSV tabular data using `csv.writer`, `csv.reader`, and row-as-dictionary parsing with `csv.DictReader`. |
| `08_json_read_write.py` | Serializing Python dictionaries to JSON files (`json.dump`, `json.load`) and JSON strings in memory (`json.dumps`, `json.loads`). |
| `09_pathlib_basics.py` | Modern object-oriented path handling with `pathlib.Path`: directory creation, path joining (`/`), existence checks, and text I/O. |
| `10_enum.py` | Defining symbolic, type-safe constant enumerations using Python's `enum.Enum`, `auto()`, and `@unique`. |

## 💡 Key points

1. **Context Managers with `with`**: Always use `with open(...) as f:` to manage file streams; it guarantees the file will be closed properly even if an error occurs.
2. **Access Modes**: `'r'` reads existing files, `'w'` truncates and overwrites, `'a'` appends to the end, and `'x'` creates exclusively (raising `FileExistsError` if the file exists).
3. **JSON Conversion**: `json.dump()` and `json.load()` operate on file objects; `json.dumps()` and `json.loads()` operate on strings in memory.
4. **CSV Newline Handling**: Always specify `newline=""` when opening CSV files for writing on Windows to prevent extra blank lines between rows.
5. **Pathlib over OS String Joining**: `pathlib.Path` uses the `/` operator to construct clean, cross-platform file paths that work seamlessly across Windows, macOS, and Linux.

## 🧠 Beginner tip

Always be cautious with `'w'` mode! Opening an existing file with `open("notes.txt", "w")` immediately wipes out all of its previous contents. If your goal is to add new text while preserving what is already there, always use `'a'` (append mode).

## 📊 Where this is used in Data Science

File handling forms the foundation of data ingestion. Data analysts and scientists read CSV, TSV, and JSON files every day to load raw records into DataFrames using tools like Pandas (`pd.read_csv()`, `pd.read_json()`). Modern data engineering pipelines rely on `pathlib` to navigate directory structures, manage batch output folders, and organize training data.

## 🛠️ Code Examples

### The `with` Context Manager (`06_with_statement.py`)
```python
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
```

### Tabular CSV Handling with `DictReader` (`07_csv_read_write.py`)
```python
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} studies {row['Course']}")
```

### JSON Serialization & Parsing (`08_json_read_write.py`)
```python
import json

data = {"name": "Hamza", "course": "Data Science"}
json_str = json.dumps(data, indent=4)  # dict -> JSON string
parsed = json.loads(json_str)          # JSON string -> dict
```

### Modern Paths with Pathlib (`09_pathlib_basics.py`)
```python
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
file_path = data_dir / "students.csv"
print(file_path.exists())
```

## 🏋️ Practice Exercises

Sharpen your file handling skills with the exercises in the practice folder:
- [Chapter 09 Exercises](../chapter_09_file_handling_exercises/README.md)

## ⏭️ What's Next

- [Chapter 10 - Object-Oriented Programming](../chapter_10_oop/README.md)
