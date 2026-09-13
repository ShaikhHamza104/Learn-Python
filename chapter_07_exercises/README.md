# 🐍 Chapter 07 Exercises — Loops Practice 🔁

Welcome to the **Chapter 07 Practice Exercises**! 🚀  
Loops are tested thoroughly here across 10 problems covering multiplication tables, list filtering, prime number checks, factorials, summations, star pattern algorithms, and reverse iterations.

---

## 📌 Exercises Overview

| File | Topic | Core Concept | Difficulty |
|---|---|---|---|
| ✖️ [`problem1.py`](./problem1.py) | Multiplication Table (`for`) | Basic iteration with `for i in range(1, 11)` | 🟢 Beginner |
| 👥 [`problem2.py`](./problem2.py) | Greet Names Starting with 'S' | List iteration and `.startswith("S")` | 🟢 Beginner |
| ⏳ [`problem3.py`](./problem3.py) | Multiplication Table (`while`) | Manual index incrementing in `while` loop | 🟢 Beginner |
| 🔢 [`problem4.py`](./problem4.py) | Prime Number Tester | Modulo division check with `break-else` | 🟡 Easy-Medium |
| ➕ [`problem5.py`](./problem5.py) | Sum of First n Numbers | Accumulator pattern with `while` | 🟢 Beginner |
| ❗ [`problem6.py`](./problem6.py) | Factorial of a Number | Product accumulation with `for` loop | 🟡 Easy-Medium |
| 🔺 [`problem7.py`](./problem7.py) | Pyramid Star Pattern | Nested loop / mathematical spacing algorithm | 🟡 Easy-Medium |
| 📐 [`problem8.py`](./problem8.py) | Right-Angled Star Triangle | Linear star growth `* * i` | 🟢 Beginner |
| 🔲 [`problem9.py`](./problem9.py) | Hollow Square Star Pattern | Boundary condition logic (`i == 1` or `j == 1`) | 🔴 Medium |
| 🔄 [`problem10.py`](./problem10.py) | Reversed Multiplication Table | Negative step `range(10, 0, -1)` | 🟢 Beginner |

---

## ✖️ Problem 1: Multiplication Table via `for` Loop (`problem1.py`)

### ❓ Objective
Write a program to print the multiplication table of a given number using a `for` loop.

### 💻 Code
```python
num = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

▶️ **Run:** `python problem1.py`

---

## 👥 Problem 2: Greeting List Filter (`problem2.py`)

### ❓ Objective
Greet all person names stored in a list `l` that start with `'S'`.

### 💻 Code
```python
names = ["Harry", "Soham", "Sachin", "Rahul", "Sam"]

for name in names:
    if name.startswith("S"):
        print(f"Hello, {name}!")
```

▶️ **Run:** `python problem2.py`

---

## ⏳ Problem 3: Multiplication Table via `while` Loop (`problem3.py`)

### ❓ Objective
Write a program to print the multiplication table of a given number using a `while` loop.

### 💻 Code
```python
num = int(input("Enter number: "))
i = 1

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
```

▶️ **Run:** `python problem3.py`

---

## 🔢 Problem 4: Prime Number Checker (`problem4.py`)

### ❓ Objective
Write a program to find whether a given number is prime or not.

### 💻 Code
```python
num = int(input("Enter number: "))

if num <= 1:
    print(f"{num} is NOT a prime number.")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is NOT a prime number.")
            break
    else:
        print(f"{num} is a PRIME number!")
```

▶️ **Run:** `python problem4.py`

---

## ➕ Problem 5: Sum of Natural Numbers (`problem5.py`)

### ❓ Objective
Write a program to find the sum of the first `n` natural numbers using a `while` loop.

### 💻 Code
```python
n = int(input("Enter n: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum:", total)
```

▶️ **Run:** `python problem5.py`

---

## ❗ Problem 6: Factorial Calculator (`problem6.py`)

### ❓ Objective
Write a program to calculate the factorial of a given number using a `for` loop.

### 💻 Code
```python
num = int(input("Enter number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")
```

▶️ **Run:** `python problem6.py`

---

## 🔺 Problem 7, 8 & 9: Star Patterns (`problem7.py`, `problem8.py`, `problem9.py`)

### Pyramid Pattern (`problem7.py`):
```python
n = 3
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
#   *
#  ***
# *****
```

### Right Triangle (`problem8.py`):
```python
n = 3
for i in range(1, n + 1):
    print("*" * i)
# *
# **
# ***
```

### Hollow Box (`problem9.py`):
```python
n = 3
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
# ***
# * *
# ***
```

---

## 🔄 Problem 10: Reversed Table (`problem10.py`)

### ❓ Objective
Print the multiplication table of `n` in reverse order (from 10 down to 1).

### 💻 Code
```python
num = int(input("Enter number: "))

for i in range(10, 0, -1):
    print(f"{num} x {i} = {num * i}")
```

▶️ **Run:** `python problem10.py`

---

## ⏭️ What's Next?
Now consolidate your logic into reusable components in **[Chapter 08 — Functions](../chapter_08/README.md)**!
