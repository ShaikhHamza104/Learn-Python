# 🐍 Chapter 08 — Functions: Modular, Reusable Code 🧩

Welcome to Chapter 8! Functions are the building blocks of maintainable software. Instead of copying and pasting code, functions allow you to define a block of logic once and invoke it anywhere with different inputs. In this chapter, you will learn how to declare functions, pass arguments, return values, handle variable arguments (`*args`), implement recursion, write one-line lambda expressions, and document code using modern Python type hints.

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_intro_function.py` | Declaring Functions | `def greet(): print("Hello!")` |
| 02 | `02_quick_quiz.py` | Greeting Function | Practical example greeting a user |
| 03 | `03_function_with_arg.py` | Parameters & Arguments | `def greet(name): print(f"Hello, {name}")` |
| 04 | `04_return.py` | Return Statement | Sending data back to the caller with `return` |
| 05 | `05_keyword_arg.py` | Keyword Arguments | Calling functions via parameter names `greet(name="Ali")` |
| 06 | `06_positional_arg.py` | Positional Arguments | Argument binding based on order |
| 07 | `07_variable_len_arg.py` | Arbitrary Arguments (`*args`) | Accepting any number of arguments |
| 08 | `08_recursion.py` | Recursion | Functions calling themselves (e.g., Factorial) |
| 09 | `09_lambda_fun.py` | Anonymous Lambda Functions | `square = lambda x: x * x` |
| 10 | `10_type_hints.py` | Modern Type Annotations | `def add(a: int, b: int) -> int:` |

---

## 🛠️ 1. Basic Function Syntax & Return Values (`01_intro_function.py`, `04_return.py`)

```python
def add_numbers(a, b):
    """Calculates and returns the sum of two numbers."""
    result = a + b
    return result

total = add_numbers(15, 25)
print("Total:", total)  # 40
```

> [!NOTE]
> If a function does not have a `return` statement, or returns without a value, Python automatically returns `None`.

---

## 🎯 2. Positional, Keyword, and Variable Arguments (`05_keyword_arg.py`, `07_variable_len_arg.py`)

```python
# Default and keyword arguments
def introduce(name, title="Student"):
    print(f"{name} is a {title}.")

introduce("Hamza")                     # Uses default title "Student"
introduce(title="Engineer", name="Ali") # Keyword arguments (order doesn't matter)

# Variable-length arguments (*args)
def sum_all(*numbers):
    # 'numbers' is received as a tuple
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # 15
```

---

## 🔁 3. Recursion (`08_recursion.py`)

Recursion occurs when a function calls itself. Every recursive function **must have a base condition** to stop the recursion from running indefinitely.

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

---

## ⚡ 4. Lambda Functions & Type Hints (`09_lambda_fun.py`, `10_type_hints.py`)

```python
# Lambda: Small anonymous one-line functions
multiply = lambda x, y: x * y
print(multiply(4, 5))  # 20

# Type hints: Improving code readability and editor autocomplete
def calculate_tax(price: float, rate: float = 0.05) -> float:
    return price * rate
```

---

## 🏋️ Practice Exercises
Sharpen your function skills with 8 exercises in **[chapter_08_exercises/](../chapter_08_exercises/README.md)**!

---

## ⏭️ What's Next?
Now learn how to interact with the file system and create custom enumerations in **[Chapter 09 — File Handling & Enums](../chapter_09/README.md)**!
