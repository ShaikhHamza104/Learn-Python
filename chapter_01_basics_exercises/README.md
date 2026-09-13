# 📚 Topic: Python Basics Practice (Exercises)

This folder contains 5 hands-on practice problems designed to reinforce your foundational Python skills. You will practice printing multi-line text, performing calculations within output statements, working with third-party speech modules, and interacting with the local operating system directory structure.

---

## 📂 What's in this folder

| File | What it teaches |
|------|------------------|
| `problem1.py` | Asks the learner to print the multi-line "Twinkle Twinkle Little Star" poem formatted across multiple lines using triple quotes (`"""`). |
| `problem2.py` | Asks the learner to print the multiplication table of 5 by evaluating arithmetic multiplication (`5 * n`) directly inside `print()` statements. |
| `problem3.py` | Asks the learner to install and import an external third-party library (`pyttsx3`) to initialize a text-to-speech engine that speaks aloud. |
| `problem4.py` | Asks the learner to import Python's standard `os` module and use `os.listdir()` to print all files and folders in a specified directory. |
| `problem5.py` | Asks the learner to document the directory inspection code from problem 4 with informative, descriptive comments explaining each line. |

---

## 💡 Key points

1. **`problem1.py` practices multi-line string formatting**: Wrapping text inside triple quotes (`"""` or `'''`) preserves line breaks and spacing exactly as typed without needing explicit newline characters.
2. **`problem2.py` practices in-line expression evaluation**: Python automatically computes arithmetic operators (such as `*` for multiplication) inside function calls before printing the resulting value.
3. **`problem3.py` practices external module integration**: Demonstrates how third-party packages installed via `pip` are imported and controlled through high-level APIs.
4. **`problem4.py` practices system inspection**: Uses `os.listdir()` and a simple `for` loop to enumerate and display real files and folders from the operating system.
5. **`problem5.py` practices explanatory code documentation**: Teaches effective use of single-line `#` comments to explain intent, parameters, and flow for future maintainers.

---

## 🧠 Beginner tip

When running `problem4.py` or `problem5.py` on Windows, change `directory_path = "/"` to `directory_path = "."` to list the files right inside your current folder. It makes the output immediately recognizable!

---

## 📊 Where this is used in Data Science

Directory listing and file inspection are common first steps in any data pipeline. Before loading tabular datasets into Pandas or processing images with computer vision libraries, data scientists use `os.listdir()` or `pathlib` to scan raw data directories, count input files, and verify file extensions (e.g., verifying all files are `.csv` or `.parquet`).

---

## 🏃 How to Run Each Exercise

Execute each problem file from your terminal:

```bash
# Problem 1: Print Multi-line Poem
python problem1.py

# Problem 2: Print Multiplication Table
python problem2.py

# Problem 3: Text-to-Speech (requires: pip install pyttsx3)
python problem3.py

# Problem 4: List Directory Contents
python problem4.py

# Problem 5: Documented Directory Listing
python problem5.py
```

---

## 📖 Related Lessons
Need a refresher on basic syntax, comments, or imports? Review the lessons in **[Chapter 01 — Basics](../chapter_01_basics/README.md)**.

---

## ⏭️ What's Next?
Ready to store dynamic values and capture user inputs? Head over to **[Chapter 02 — Variables & Data Types](../chapter_02_variables_datatypes/README.md)**!
