# 📚 Topic: File Handling Practice (Exercises)

Hands-on exercises applying file reading, keyword detection, high-score game state persistence, batch file generation across directories, sensitive word censorship, log mining and line tracing, file duplication, content comparison, and file wiping.

## 📂 What's in this folder

| File | Description |
|---|---|
| `problem1.py` | Reads `poems.txt` and checks whether the word `"twinkle"` is present using the `in` operator. |
| `problem2.py` | Simulates a game that generates random scores and updates `highscore.txt` whenever the high score is broken. |
| `problem3.py` | Generates multiplication tables for numbers 2 through 20 and writes each table into its own text file inside the `table/` directory. |
| `problem4.py` | Reads `problem4.txt` and censors the word `"Donkey"` by replacing it with `"#####"`. |
| `problem5.py` | Censoring multiple flagged words from a list by replacing each word dynamically with `"#" * len(word)`. |
| `problem6.py` | Mines a server log file (`log.txt`) to determine whether it contains the word `"python"` using case-insensitive search. |
| `problem7.py` | Reads `log.txt` line-by-line using `.readlines()` to identify and report the exact line number where `"Python"` first occurs. |
| `problem8.py` | Copies the entire content of `this.txt` into a duplicate file named `this_copy.txt`. |
| `problem9.py` | Compares the contents of `file1.txt` and `file2.txt` to verify whether the two files are identical. |
| `problem10.py` | Clears/wipes the entire contents of a file by opening it in write mode (`'w'`) and writing an empty string. |
| `problem11.py` | Reads the contents of `file1.txt` preparing it for file renaming. |

## 💡 Key points

1. **Problem 1 (`problem1.py`)**: Demonstrates basic text inspection by reading an entire file into memory and checking for substring existence with `in`.
2. **Problem 2 (`problem2.py`)**: Implements score persistence by reading an existing file, casting the string score to `int`, and overwriting with new record values.
3. **Problem 3 (`problem3.py`)**: Uses nested loops and dynamic filenames (`f"table{i}.txt"`) to batch-create tabular text files.
4. **Problem 4 (`problem4.py`)**: Performs in-place text sanitization by reading, modifying content with `.replace()`, and writing back using `'w'` mode.
5. **Problem 5 (`problem5.py`)**: Masks varying-length sensitive words dynamically by matching the replacement mask length with `len(word)`.
6. **Problem 6 (`problem6.py`)**: Normalizes log text and query terms to lowercase (`.lower()`) to perform case-insensitive pattern detection.
7. **Problem 7 (`problem7.py`)**: Uses `.readlines()` and a line counter to pinpoint the exact line index of an event in a log file.
8. **Problem 8 (`problem8.py`)**: Implements file duplication by reading data from a source file and writing it to a target destination file.
9. **Problem 9 (`problem9.py`)**: Determines file equality by comparing read strings (`data1 == data2`).
10. **Problem 10 (`problem10.py`)**: Demonstrates file truncation by opening with `'w'` mode and writing an empty string `""`.
11. **Problem 11 (`problem11.py`)**: Reads a file's content into memory ahead of renaming or moving operations.

## 🧠 Beginner tip

When reading files that may be empty (like `highscore.txt` in `problem2.py`), always verify that the content string is non-empty before calling `int()` on it. Calling `int("")` raises a `ValueError: invalid literal for int() with base 10: ''`.

## 📊 Where this is used in Data Science

Log mining and text search are routine tasks in MLOps and production data engineering: monitoring training logs, tracking pipeline execution steps, and identifying data pipeline exceptions. Batch generating files and reading tabular records mirror distributed dataset partitioning and chunked file processing.

## 🏃 How to Run Each Exercise

Run each exercise script from your terminal:

```bash
python problem1.py
python problem2.py
python problem3.py
python problem4.py
python problem5.py
python problem6.py
python problem7.py
python problem8.py
python problem9.py
python problem10.py
python problem11.py
```

## 📖 Related Lessons

- [Chapter 09 - File Handling](../chapter_09_file_handling/README.md)

## ⏭️ What's Next

- [Chapter 10 - Object-Oriented Programming](../chapter_10_oop/README.md)
