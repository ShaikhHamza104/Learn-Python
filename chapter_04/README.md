# 🐍 Chapter 04 — Lists & Tuples: Ordered Collections 📋

Welcome to Chapter 4! In the previous chapter, you learned how to handle individual pieces of text using strings. Now, you will learn how to store, organize, and transform **collections** of data using **Lists** and **Tuples**.

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_list.py` | Introduction to Lists | `items = ["apple", 42, 3.14, True]` |
| 02 | `02_operation_list.py` | Operations on Lists | Indexing, slicing, repetition, and membership (`in`) |
| 03 | `03_list_method.py` | Built-in List Methods | `.append()`, `.sort()`, `.reverse()`, `.pop()`, `.remove()` |
| 04 | `04_tuple.py` | Introduction to Tuples | `t = (1, 2, 3)`, singleton tuple `t = (1,)` |
| 05 | `05_operation_tuple.py` | Tuple Operations | Concatenation, slicing, immutability checks |
| 06 | `06_tuple_method.py` | Built-in Tuple Methods | `t.count(value)`, `t.index(value)` |
| 07 | `07_enumerate.py` | Looping with Index | `for idx, val in enumerate(li):` |
| 08 | `08_dir_method.py` | Introspection with `dir()` | Inspecting available methods on objects |
| 09 | `09_list_comprehension.py` | List Comprehensions | `[x**2 for x in range(10) if x % 2 == 0]` |
| 10 | `10_namedtuple.py` | Named Tuples | `Point = namedtuple('Point', ['x', 'y'])` |

---

## 📝 1. Lists: Dynamic & Mutable (`01_list.py`, `02_operation_list.py`)

A **list** is an ordered, mutable sequence of items enclosed in square brackets `[]`. Lists can hold values of different data types.

```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
mixed = ["text", 25, 3.14, True]

# Indexing & Slicing
print(fruits[0])     # 'apple'
print(fruits[-1])    # 'cherry'
print(fruits[1:3])   # ['banana', 'cherry']

# Lists are MUTABLE: you can update items directly
fruits[1] = "blueberry"
print(fruits)        # ['apple', 'blueberry', 'cherry']
```

▶️ **Run:** `python 01_list.py`

---

## 🛠️ 2. List Methods (`03_list_method.py`)

Python includes powerful built-in methods to manipulate lists in place:

```python
numbers = [4, 2, 8, 1, 5]

numbers.append(10)      # Adds 10 to the end -> [4, 2, 8, 1, 5, 10]
numbers.sort()          # Sorts ascending  -> [1, 2, 4, 5, 8, 10]
numbers.reverse()       # Reverses order   -> [10, 8, 5, 4, 2, 1]
numbers.insert(2, 99)   # Inserts 99 at index 2
popped = numbers.pop()  # Removes and returns last item
numbers.remove(99)      # Removes first occurrence of 99
```

> [!TIP]
> Notice that `numbers.sort()` modifies the list **in place** and returns `None`. Do not assign `res = numbers.sort()`!

---

## 🔒 3. Tuples: Immutable Sequences (`04_tuple.py`, `05_operation_tuple.py`, `06_tuple_method.py`)

A **tuple** is an ordered, **immutable** sequence enclosed in parentheses `()`. Once created, its items cannot be added, removed, or modified.

```python
coordinates = (10, 20)
singleton = (5,)  # Comma is REQUIRED for a single-element tuple!

# coordinates[0] = 15  # ❌ Raises TypeError: 'tuple' object does not support item assignment
```

### Tuple Methods:
Tuples only have two built-in methods because they cannot be modified:
```python
t = (1, 2, 3, 2, 2, 4)
print(t.count(2))  # 3 (counts how many times 2 appears)
print(t.index(3))  # 2 (first index where 3 is located)
```

---

## 🔢 4. `enumerate()` (`07_enumerate.py`)

When looping over a sequence, `enumerate()` gives you both the **index** and the **value** together, eliminating the need for manual counter variables.

```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")
```

**Output:**
```
1. red
2. green
3. blue
```

---

## 🔍 5. Object Introspection with `dir()` (`08_dir_method.py`)

The built-in `dir()` function returns a list of all valid attributes and methods for any object.

```python
my_list = [1, 2]
print(dir(my_list))  # shows __iter__, append, pop, sort, etc.
```

---

## ⚡ 6. List Comprehensions (`09_list_comprehension.py`)

List comprehensions provide a concise, readable way to generate new lists based on existing iterables.

```python
# Syntax: [expression for item in iterable if condition]
squares = [x**2 for x in range(1, 6)]
# Result: [1, 4, 9, 16, 25]

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# Result: [4, 16, 36, 64, 100]
```

---

## 🏷️ 7. `namedtuple` (`10_namedtuple.py`)

From `collections import namedtuple`. A `namedtuple` creates tuple subclasses where elements are accessible by attribute name as well as index.

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(x=10, y=20)

print(p.x, p.y)     # 10 20 (Readable!)
print(p[0], p[1])   # 10 20 (Indexable!)

# Helpful helper methods:
data = p._asdict()                 # {'x': 10, 'y': 20}
p2 = p._replace(x=30)              # Point(x=30, y=20)
```

---

## 🆚 Lists vs. Tuples

| Feature | List (`list`) | Tuple (`tuple`) |
|---|---|---|
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` or `(1,)` |
| **Mutability** | Mutable (can change) | Immutable (read-only) |
| **Methods** | `.append()`, `.pop()`, `.sort()`, etc. | `.count()`, `.index()` |
| **Memory & Speed** | Slightly more memory | Lightweight and faster |
| **Use Case** | Collections that change over time | Fixed records, coordinates, dictionary keys |

---

## 🏋️ Practice Exercises
Ready to test your knowledge? Head over to **[chapter_04_exercises/](../chapter_04_exercises/README.md)** for 5 hands-on practice problems!

---

## ⏭️ What's Next?
Next up is **[Chapter 05 — Dictionaries & Sets](../chapter_05/README.md)**, where you will learn how to store key-value mappings and unique elements!
