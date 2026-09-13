# 📚 Topic: Python Basics (First Program, Comments & Modules)

Python is known for its clean, readable syntax that reads almost like plain English. This chapter introduces the foundations of how Python scripts execute: printing output to your screen, adding explanatory notes (comments) for human readers, and importing external code libraries (modules) so you don't have to reinvent the wheel.

---

## 📂 What's in this folder

| File | What it teaches |
|------|------------------|
| `01_hello_world.py` | Printing messages to the console with `print()` and using the standard `main()` execution pattern. |
| `02_comment_example.py` | Writing single-line comments (`#`), multi-line docstrings (`"""`), and commenting out code for debugging. |
| `02_module_example.py` | Importing third-party modules (like `pyjokes`) to bring pre-written features into your script. |

---

## 💡 Key points

1. **`print()` is your window into the program**: It sends text, numbers, and calculation results directly to the console so you can inspect what your code is doing.
2. **Comments are strictly for humans**: Python completely ignores everything after a `#` or inside an unassigned triple-quoted string (`"""`), making them perfect for explaining *why* code was written.
3. **Modules save you time**: Python has a massive ecosystem of built-in and community modules; using the `import` keyword allows you to reuse reliable, tested code with a single line.

---

## 🧠 Beginner tip

Open `01_hello_world.py`, change the text inside `print("Hello, world!")` to your name or a custom greeting, and run it in your terminal. Tweaking working code and seeing immediate feedback is the fastest way to get comfortable with Python!

---

## 📊 Where this is used in Data Science

While printing and commenting are universal programming skills, running standalone scripts and importing modules form the foundation of every data science workflow. Before training complex machine learning models, data scientists frequently use `print()` statements and logging to inspect dataset shapes, verify sample rows, and track pipeline progress. Furthermore, every data analysis project in Python starts by importing specialized libraries—such as NumPy for numerical operations, Pandas for tabular data, and Matplotlib for charting.

---

## 🛠️ Code Examples & Running the Files

### 1. Hello World (`01_hello_world.py`)
```python
def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()
```
Run with:
```bash
python 01_hello_world.py
```

### 2. Comments & Docstrings (`02_comment_example.py`)
```python
# Single-line comment: explain the "why", not the obvious "what"
price = 100  # Base price before taxes

"""
Docstrings can span multiple lines.
They are commonly placed at the top of files or functions.
"""
```

### 3. Using Modules (`02_module_example.py`)
```python
import pyjokes

# Fetch a random programmer joke from an external module
joke = pyjokes.get_joke()
print(joke)
```

---

## 🏋️ Practice Exercises
Ready to test what you've learned? Check out the hands-on problems in **[chapter_01_basics_exercises/](../chapter_01_basics_exercises/README.md)**!

---

## ⏭️ What's Next?
Continue your journey in **[Chapter 02 — Variables & Data Types](../chapter_02_variables_datatypes/README.md)**, where you will learn how to store values, capture user input, and perform arithmetic!
