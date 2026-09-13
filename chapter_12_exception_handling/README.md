# 📚 Topic: Exception Handling & Logging

Exceptions are runtime errors that halt program execution if left unhandled. Python provides a robust error-handling mechanism using `try`, `except`, `else`, and `finally` blocks, along with the ability to raise custom exceptions and record persistent diagnostics with the built-in `logging` module. Mastering exception handling ensures your programs fail gracefully, validate constraints cleanly, and keep detailed audit trails.

---

## 📂 What's in this folder

| File | What it teaches |
| --- | --- |
| `01_intro_exception.py` | Basic `try-except` block catching `ValueError` from invalid user input |
| `02_multiple_except_block.py` | Handling distinct errors (`ValueError`, `IndexError`) with separate `except` clauses |
| `03_try_except_else.py` | Using the `else` clause to execute code only when no exceptions occur |
| `04_finally_block.py` | Executing the `finally` block for guaranteed cleanup regardless of exceptions |
| `05_file_handling.py` | Catching `FileNotFoundError` during file operations and ensuring cleanup |
| `06_class_error.py` | Catching `AttributeError` when accessing undefined instance attributes in classes |
| `07_raise_error.py` | Manually triggering built-in exceptions using the `raise` keyword |
| `08_custom_error_without_using_constructor.py` | Creating a simple custom exception class subclassing `Exception` |
| `09_custom_error_with_using_constructor.py` | Building custom exceptions with an `__init__` constructor for detailed error messages |
| `10_zero_division_error.py` | Capturing `ZeroDivisionError` and `ValueError` during arithmetic calculations |
| `11_logging_basics.py` | Setting up `logging.basicConfig`, the 5 log severity levels, and writing logs to `app.log` |
| `12_exception_logging.py` | Recording errors and full stack traces using `logging.error()` and `logging.exception()` in `errors.log` |

---

## 💡 Key points

1. **The `try-except` Guard (`01_intro_exception.py`)**: Wrap risky operations (such as converting string input with `int()`) inside a `try` block and provide fallback handling in an `except ValueError:` block to prevent sudden crashes.
2. **Specific Exception Handling (`02_multiple_except_block.py`)**: Multiple `except` blocks let you respond differently to different error types, such as handling a `ValueError` for bad input conversion separately from an `IndexError` for out-of-bounds list indexing.
3. **The `else` Clause (`03_try_except_else.py`)**: Code in an `else` block runs only if the `try` block finishes without raising any exceptions—ideal for running downstream logic like calculating and printing a multiplication table.
4. **Guaranteed Execution with `finally` (`04_finally_block.py`)**: The `finally` block runs unconditionally, whether an exception occurred, was handled, or never happened at all—perfect for closing connections or printing exit messages.
5. **Safe File Operations (`05_file_handling.py`)**: Catching `FileNotFoundError` prevents crashes when a requested filename does not exist, while placing `f.close()` in `finally` guarantees resource release.
6. **Handling Missing Attributes (`06_class_error.py`)**: Attempting to access an undefined attribute on a class instance (like `e1.gender` on an `Empolyee` object) raises `AttributeError`, which can be caught to prevent crashing before calling methods like `e1.show()`.
7. **Raising Exceptions Manually (`07_raise_error.py`)**: Use the `raise` keyword to trigger an exception deliberately when business rules are violated (e.g., raising `ValueError` when `age < 18`).
8. **Subclassing `Exception` (`08_custom_error_without_using_constructor.py`)**: Define domain-specific errors by inheriting from `Exception` (`class InvalidAge(Exception): pass`), allowing you to catch custom failure states precisely.
9. **Parameterized Custom Exceptions (`09_custom_error_with_using_constructor.py`)**: Adding an `__init__` constructor to your custom exception class allows you to pass custom error messages and metadata when raising the exception (e.g., `InvalidPass("Password must contain at least 10 letters...")`).
10. **Preventing Division by Zero (`10_zero_division_error.py`)**: Dividing by zero raises `ZeroDivisionError`; pairing it with `ValueError` guards user-facing division operations against both invalid types and zero denominators.
11. **Logging Fundamentals (`11_logging_basics.py`)**: The `logging` module offers 5 standard severity levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`). Configuring `logging.basicConfig(filename="app.log", level=logging.INFO, force=True)` saves timestamped messages to disk permanently rather than ephemeral console prints.
12. **Exception Logging with Tracebacks (`12_exception_logging.py`)**: Inside an `except` block, calling `logging.exception()` records the error message alongside the complete stack traceback to your log file (`errors.log`), pinpointing exact line numbers and failure causes for unattended scripts.

---

## 🧠 Beginner tip

Always catch **specific** exceptions (e.g., `except ValueError:`, `except FileNotFoundError:`) instead of using a bare `except:` or broad `except Exception:`. Bare `except` catches everything, including `KeyboardInterrupt` (`Ctrl+C`) and `SystemExit`, making programs hard to terminate and masking silent bugs. When logging errors inside an `except` block, prefer `logging.exception()` over `logging.error()` because `logging.exception()` automatically captures the full stack trace.

---

## 📊 Where this is used in Data Science

- **Data Ingestion Pipelines**: Data files often have missing columns, malformed timestamps, or corrupted rows. Wrapping file parsers and data loaders in `try-except` prevents a single bad record from terminating hours of pipeline processing.
- **API & Database Connections**: Network drops, query timeouts, and rate limits raise specific connection errors. Proper exception handling allows ETL pipelines to implement retry strategies or failover gracefully.
- **Automated Long-Running Jobs**: Model training and batch scoring jobs running overnight on remote servers cannot rely on `print()`. Writing timestamped logs via `logging.basicConfig()` and capturing stack traces with `logging.exception()` enables engineers to inspect 3 AM failures and identify the exact offending row or tensor shape.

---

## 🛠️ Code Examples

### Basic `try-except-else-finally`
```python
try:
    num = int(input("Enter denominator: "))
    result = 100 / num
except ValueError:
    print("Please enter an integer!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Calculation attempt finished.")
```

### Custom Exception Class
```python
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age {age}: must be 18 or older.")
        self.age = age

age = 15
if age < 18:
    raise InvalidAgeError(age)
```

### Logging to File with Full Stack Trace
```python
import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    with open("dataset.csv", "r") as f:
        data = f.read()
except FileNotFoundError:
    logging.exception("Data ingestion failed - dataset missing:")
```

---

## 🏋️ Practice Exercises

Sharpen your exception handling and defensive programming skills with hands-on practice problems in **[chapter_12_exception_handling_exercises/](../chapter_12_exception_handling_exercises/README.md)**!

---

## ⏭️ What's Next

Learn how to organize code across multiple files, create reusable modules, and bundle packages in **[Chapter 13 — Modules & Packages](../chapter_13_modules_packages/README.md)**!
