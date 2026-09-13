# 📚 Topic: Exception Handling Practice (Exercises)

This folder contains 10 hands-on practice problems reinforcing Python exception handling techniques. The exercises progress from basic `try-except` blocks for user input and arithmetic errors, to file stream safety with `finally`, up to custom exception hierarchies with parameterized constructors.

---

## 📂 What's in this folder

| File | Description |
| --- | --- |
| `problem1.py` | Validating integer user input and catching `ValueError` |
| `problem2.py` | Safe number division with separate `except` blocks for `ValueError` and `ZeroDivisionError` |
| `problem3.py` | Directory listing and safe file opening with `try-except` handling `FileNotFoundError` |
| `problem4.py` | Interactive file reader and writer using `finally` for resource cleanup |
| `problem5.py` | Copying file contents from one file to another with `FileNotFoundError` and `PermissionError` handling |
| `problem6.py` | A `Rectangle` class raising `ValueError` in `__init__` if dimensions are zero or negative |
| `problem7.py` | Defining a custom `NegativeValueError` exception and raising it for values below zero |
| `problem8.py` | Defining a parameterless `InvalidAgeError` exception for ages outside 1–150 |
| `problem9.py` | Defining a parameterized `TemperatureError` exception storing message and temperature below absolute zero |
| `problem10.py` | Dividing two user-entered numbers handling `ZeroDivisionError` with an `else` block |

---

## 💡 Key points

1. **Integer Input Validation (`problem1.py`)**: Wrapping `int(input(...))` in a `try-except ValueError` catches character and decimal inputs before they cause program crashes.
2. **Multiple Catch Blocks (`problem2.py`)**: Providing separate `except ValueError:` and `except ZeroDivisionError:` handlers ensures accurate diagnostic feedback for distinct input errors.
3. **Missing File Protection (`problem3.py`)**: Before opening a user-specified filename from `os.listdir()`, catching `FileNotFoundError` prevents unhandled termination if the filename does not exist.
4. **Interactive File Management (`problem4.py`)**: Demonstrates menu-driven file reading and writing with guaranteed stream closure in a `finally` block even when reading raises an error.
5. **Robust File Copying (`problem5.py`)**: Guarding file transfer operations against both `FileNotFoundError` (source file missing) and `PermissionError` (restricted disk access) provides safe file replication.
6. **Constructor Validation (`problem6.py`)**: Validating length and width inside `Rectangle.__init__` and raising `ValueError` for non-positive inputs enforces invariants before calculating area and perimeter.
7. **Custom Exception Classes (`problem7.py`)**: Subclassing `Exception` (`class NegativeValueError(Exception): pass`) creates clear domain-specific errors triggered by `raise NegativeValueError` when `n < 0`.
8. **Range Constraints with Custom Errors (`problem8.py`)**: Using a custom `InvalidAgeError` class cleanly signals validation failure when an input age falls outside the sensible range `(0 < age <= 150)`.
9. **Custom Exception Attributes (`problem9.py`)**: Adding an `__init__(self, m, temp)` constructor to `TemperatureError` allows exception instances to retain the invalid temperature value and error message when below absolute zero (`-273.15 °C`).
10. **Arithmetic Division with `else` (`problem10.py`)**: Performing division inside `try`, catching `ZeroDivisionError`, and using `else` to output results guarantees clean separation between error reporting and successful display.

---

## 🧠 Beginner tip

When defining custom exception classes, always inherit from Python's built-in `Exception` (or a more specific built-in exception like `ValueError`), never from `BaseException`. Inheriting from `Exception` allows standard `except Exception:` handlers to catch your errors, whereas `BaseException` is reserved for system-exiting events like `KeyboardInterrupt` and `SystemExit`.

---

## 📊 Where this is used in Data Science

- **Sanitizing User Queries & Parameters**: Machine learning web services (FastAPI/Flask) validate numerical parameters (learning rates, batch sizes, cluster counts) using custom exceptions to reject out-of-bounds configurations before launching GPU computations.
- **Handling Corrupted Batch Files**: Data loaders scanning directories for raw CSVs or Parquet files catch `FileNotFoundError` and `PermissionError` to log skipped files and continue batch ingestion smoothly.
- **Physics & Domain Boundary Checks**: Feature engineering pipelines processing sensor telemetry (temperatures, pressures, velocities) use custom exceptions to catch physically impossible sensor readings (such as temperatures below absolute zero) before calculating feature aggregates.

---

## 🏃 How to Run Each Exercise

Run each problem from your terminal using Python:

```bash
# Problem 1: Validate integer input
python problem1.py

# Problem 2: Safe division with multiple except blocks
python problem2.py

# Problem 3: Safe file opening with directory check
python problem3.py

# Problem 4: File read/write menu with finally cleanup
python problem4.py

# Problem 5: Safe file copy with permission handling
python problem5.py

# Problem 6: Rectangle constructor input validation
python problem6.py

# Problem 7: Custom NegativeValueError
python problem7.py

# Problem 8: Custom InvalidAgeError
python problem8.py

# Problem 9: Parameterized TemperatureError
python problem9.py

# Problem 10: Division with ZeroDivisionError and else block
python problem10.py
```

---

## 📖 Related Lessons

Review the complete syntax and examples for `try-except-else-finally` and `logging` in **[Chapter 12 — Exception Handling & Logging](../chapter_12_exception_handling/README.md)**.

---

## ⏭️ What's Next

Move to **[Chapter 13 — Modules & Packages](../chapter_13_modules_packages/README.md)** to learn how to organize code into reusable modules, manage package namespaces, and use `__init__.py`.
