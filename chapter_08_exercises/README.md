# 🐍 Chapter 08 Exercises — Functions Practice 🧩

Welcome to the **Chapter 08 Practice Exercises**! 🚀  
These 8 problems test your ability to design clean functions, perform conversions, implement recursion, manipulate print buffers, strip list strings, and format multiplication outputs.

---

## 📌 Exercises Overview

| File | Topic | Core Concept | Difficulty |
|---|---|---|---|
| 🏆 [`problem1.py`](./problem1.py) | Greatest of Three Numbers | Multi-branch comparison in functions | 🟢 Beginner |
| 🌡️ [`problem2.py`](./problem2.py) | Celsius to Fahrenheit | Arithmetic formula in function return | 🟢 Beginner |
| 🖨️ [`problem3.py`](./problem3.py) | Suppress Newline in `print` | The `end=" "` parameter of `print()` | 🟢 Beginner |
| 🔁 [`problem4.py`](./problem4.py) | Recursive Natural Sum | Base condition & recursive step | 🟡 Easy-Medium |
| 🔻 [`problem5.py`](./problem5.py) | Inverted Star Pattern | Function with loop and string replication | 🟢 Beginner |
| 📏 [`problem6.py`](./problem6.py) | Inches to Centimeters | Unit conversion formula (`* 2.54`) | 🟢 Beginner |
| 🧹 [`problem7.py`](./problem7.py) | Strip & Remove Word from List | List comprehension with `.strip()` & filtering | 🟡 Easy-Medium |
| ✖️ [`problem8.py`](./problem8.py) | Function Multiplication Table | Parameterized table generator | 🟢 Beginner |

---

## 🏆 Problem 1: Greatest of Three Numbers (`problem1.py`)

### 💻 Code
```python
def find_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

print("Greatest:", find_greatest(12, 45, 23))  # 45
```

▶️ **Run:** `python problem1.py`

---

## 🌡️ Problem 2: Celsius to Fahrenheit (`problem2.py`)

### 💻 Code
```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("37°C in Fahrenheit:", celsius_to_fahrenheit(37))  # 98.6°F
```

▶️ **Run:** `python problem2.py`

---

## 🖨️ Problem 3: Suppress Newline in `print()` (`problem3.py`)

### 💻 Code
```python
print("Hello", end=" ")
print("World!")
# Output: Hello World!
```
By default, `print()` appends a newline (`end="\n"`). Setting `end=" "` or `end=""` keeps subsequent print outputs on the same line.

▶️ **Run:** `python problem3.py`

---

## 🔁 Problem 4: Recursive Natural Sum (`problem4.py`)

### 💻 Code
```python
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 1)

print("Sum of 1 to 5:", recursive_sum(5))  # 15
```

▶️ **Run:** `python problem4.py`

---

## 🔻 Problem 5: Inverted Star Pattern (`problem5.py`)

### 💻 Code
```python
def print_inverted_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

print_inverted_pattern(3)
# ***
# **
# *
```

▶️ **Run:** `python problem5.py`

---

## 📏 Problem 6: Inches to Centimeters (`problem6.py`)

### 💻 Code
```python
def inches_to_cm(inches):
    return inches * 2.54

print("10 inches in cm:", inches_to_cm(10))  # 25.4 cm
```

▶️ **Run:** `python problem6.py`

---

## 🧹 Problem 7: Strip and Remove Word (`problem7.py`)

### 💻 Code
```python
def remove_and_strip(word_list, target_word):
    cleaned = [w.strip() for w in word_list if w.strip() != target_word]
    return cleaned

items = ["  apple ", "banana", " apple", "cherry "]
print(remove_and_strip(items, "apple"))  # ['banana', 'cherry']
```

▶️ **Run:** `python problem7.py`

---

## ✖️ Problem 8: Multiplication Table Function (`problem8.py`)

### 💻 Code
```python
def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

print_table(7)
```

▶️ **Run:** `python problem8.py`

---

## ⏭️ What's Next?
Next, learn how to persist data into text, CSV, and JSON files, plus working with Enums, in **[Chapter 09 — File Handling & Enums](../chapter_09/README.md)**!
