# 🐍 Chapter 07 — Loops: Automating Repetition in Python 🔁

Welcome to Chapter 7! Repetition is what computers do best. Loops allow you to execute a block of code dozens, thousands, or millions of times without writing duplicate lines. In this chapter, you will master `while` loops, `for` loops, range generation, loop control statements (`break`, `continue`, `pass`), and Python's unique `for-else` construct.

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_loop.py` | Introduction to Loops | The concept of repeating tasks |
| 02 | `02_while_loop.py` | The `while` Loop | `while condition: do_something()` |
| 03 | `03_list_using_while.py` | Iterating with While | Index-based traversal of lists |
| 04 | `04_for_loop.py` | The `for` Loop | `for item in collection:` |
| 05 | `05_range.py` | Generating Sequences with `range()` | `range(start, stop, step)` |
| 06 | `06_for_with_else.py` | Loops with `else` Clause | Code that executes when a loop finishes cleanly |
| 07 | `07_break_and_continue.py` | Loop Control Statements | Exiting loops early and skipping iterations |
| 08 | `08_pass.py` | The `pass` Statement | Placeholder null statement |

---

## ⏳ 1. The `while` Loop (`02_while_loop.py`, `03_list_using_while.py`)

A `while` loop executes as long as a condition evaluates to `True`.

```python
count = 1
while count <= 5:
    print("Count:", count)
    count += 1  # ⚠️ Don't forget to update your counter, or loop will run forever!
```

---

## 🔄 2. The `for` Loop and `range()` (`04_for_loop.py`, `05_range.py`)

The `for` loop is Python's primary tool for iterating over sequences (lists, strings, tuples, dictionaries, and ranges).

```python
# Iterating over a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("Fruit:", fruit)

# Using range(start, stop, step)
# Note: 'stop' is exclusive!
for i in range(1, 10, 2):
    print(i)  # Prints: 1, 3, 5, 7, 9
```

---

## 🚪 3. `break`, `continue`, and `pass` (`07_break_and_continue.py`, `08_pass.py`)

```python
# break: Exits the loop immediately
for i in range(1, 10):
    if i == 5:
        break
    print(i)  # Prints 1, 2, 3, 4

# continue: Skips the rest of the current iteration and jumps to next
for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # Prints 1, 2, 4, 5 (skips 3)

# pass: A placeholder that does nothing (syntactically required empty block)
for i in range(5):
    pass  # Will implement later
```

---

## 🧩 4. `for-else` and `while-else` (`06_for_with_else.py`)

Python loops have an optional `else` block! It runs **only if the loop finishes normally without encountering a `break`**.

```python
# Searching for a prime number
n = 7
for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print(f"{n} is Prime!")  # Runs because loop completed without break
```

---

## 🏋️ Practice Exercises
Put your loop skills to the test with 10 comprehensive problems in **[chapter_07_exercises/](../chapter_07_exercises/README.md)**!

---

## ⏭️ What's Next?
Now that you can make decisions and loop, learn how to package reusable logic in **[Chapter 08 — Functions](../chapter_08/README.md)**!
