# 🐍 Chapter 17 Exercises — Iterators & Generators Practice ⚙️

Welcome to the **Chapter 17 Practice Exercises**! 🚀  
These exercises test your ability to build custom iterable and iterator objects, implement memory-efficient generator functions using `yield`, and compare space complexities with generator expressions.

---

## 📌 Exercises Overview

| File | Challenge Topic | Core Concept | Difficulty |
|---|---|---|---|
| ⏳ [`problem1.py`](./problem1.py) | Custom Countdown Iterator | Implementing `__iter__()`, `__next__()`, & `StopIteration` | 🟡 Easy-Medium |
| 🌀 [`problem2.py`](./problem2.py) | Fibonacci Generator Function | Infinite stream generation using `yield` | 🟡 Easy-Medium |
| 📊 [`problem3.py`](./problem3.py) | Memory Benchmark | `sys.getsizeof()` comparison: generator vs list | 🟢 Beginner |

---

## ⏳ Challenge 1: Custom Countdown Iterator (`problem1.py`)

### ❓ Objective
Write a custom iterable class `Countdown` that takes a starting integer and counts down to 1, raising `StopIteration` when complete.

### 💡 Example Solution
```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# Test:
for n in Countdown(5):
    print(n)  # 5, 4, 3, 2, 1
```

---

## 🌀 Challenge 2: Fibonacci Generator Function (`problem2.py`)

### ❓ Objective
Write a generator function `fibonacci_gen(limit)` that yields Fibonacci numbers up to `limit` without storing the whole sequence in a list.

### 💡 Example Solution
```python
def fibonacci_gen(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Test:
for num in fibonacci_gen(8):
    print(num)  # 0, 1, 1, 2, 3, 5, 8, 13
```

---

## 📊 Challenge 3: Generator Expression Memory Profiler (`problem3.py`)

### ❓ Objective
Create a script that generates the squares of numbers from 1 to 100,000 using both a list comprehension and a generator expression. Print and compare the memory consumed by both objects using `sys.getsizeof()`.

### 💡 Example Solution
```python
import sys

# List comprehension:
list_comp = [x**2 for x in range(100000)]

# Generator expression:
gen_exp = (x**2 for x in range(100000))

print("List memory:", sys.getsizeof(list_comp), "bytes")
print("Generator memory:", sys.getsizeof(gen_exp), "bytes")
```

---

## ⏭️ What's Next?
Next, discover high-performance standard library iterator tools in **[Chapter 18 — Itertools Module](../chapter_18_itertools/README.md)**!
