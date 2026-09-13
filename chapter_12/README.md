# 🐍 Chapter 12 — Exception Handling & Logging: Building Fault-Tolerant Code 🛡️

Welcome to Chapter 12! Real-world software runs into unexpected situations: missing files, invalid user input, network dropouts, or division by zero. **Exception Handling** enables your programs to anticipate, catch, and recover from errors gracefully without crashing. In this chapter, you will master `try-except-else-finally`, raising exceptions, authoring custom exception classes, and recording error traces with Python's standard `logging` library.

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_intro_exception.py` | Introduction to Exceptions | Wrapping risky code in `try-except` |
| 02 | `02_multiple_except_block.py` | Multiple Except Blocks | Handling `ValueError`, `TypeError`, `ZeroDivisionError` separately |
| 03 | `03_try_except_else.py` | The `else` Block | Runs only when **no** exceptions were raised |
| 04 | `04_finally_block.py` | The `finally` Block | Cleanup block that **always** runs (even after `return`) |
| 05 | `05_file_handling.py` | Safe File Handling | Handling `FileNotFoundError` and `PermissionError` |
| 06 | `06_class_error.py` | Built-in Exception Hierarchy | Exploring `BaseException` and `Exception` |
| 07 | `07_raise_error.py` | Raising Exceptions | Manually triggering errors with `raise` |
| 08 | `08_custom_error_without_using_constructor.py` | Custom Exception Class | Subclassing `Exception` |
| 09 | `09_custom_error_with_using_constructor.py` | Parameterized Custom Exception | Passing custom attributes into exception classes |
| 10 | `10_zero_division_error.py` | Handling Division by Zero | Safely capturing mathematical errors |
| 11 | `11_logging_basics.py` | Logging Module Basics | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |
| 12 | `12_exception_logging.py` | Exception Logging | Capturing stack traces with `logging.exception()` |

---

## 🛡️ 1. The `try-except-else-finally` Structure (`01_intro_exception.py` – `04_finally_block.py`)

```python
try:
    num = int(input("Enter a positive number: "))
    if num <= 0:
        raise ValueError("Number must be greater than zero!")
    result = 100 / num
except ValueError as ve:
    print("Invalid Input:", ve)
except ZeroDivisionError:
    print("Cannot divide 100 by zero!")
else:
    # Runs ONLY if try block succeeded without error
    print("Computation succeeded! Result:", result)
finally:
    # ALWAYS executes (used for resource cleanup)
    print("Execution complete.")
```

---

## ⚠️ 2. Raising & Custom Exceptions (`07_raise_error.py` – `09_custom_error_with_using_constructor.py`)

You can define domain-specific exceptions by inheriting from the built-in `Exception` class:

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Attempted to withdraw ₹{amount}, but balance is only ₹{balance}!")
        self.balance = balance
        self.amount = amount

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount
```

---

## 📝 3. Logging Basics & Stack Traces (`11_logging_basics.py`, `12_exception_logging.py`)

`print()` statements disappear into the console; `logging` records timestamps, severity levels, and stack traces into persistent log files.

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started.")

try:
    1 / 0
except ZeroDivisionError:
    # logging.exception automatically captures full traceback!
    logging.exception("An error occurred during division.")
```

---

## 🏋️ Practice Exercises
Harden your code against file errors, index bounds, and division crashes across 10 exercises in **[chapter_12_exercises/](../chapter_12_exercises/README.md)**!

---

## ⏭️ What's Next?
Now learn how to structure multi-file projects in **[Chapter 13 — Modules & Packages](../chapter_13/README.md)**!
