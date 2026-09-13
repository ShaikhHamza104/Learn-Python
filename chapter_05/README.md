# 🐍 Chapter 05 — Dictionaries & Sets: Key-Value & Unique Collections 🗝️

Welcome to Chapter 5! In this chapter, you will master two of Python's most essential data structures: **Dictionaries** (for fast, associative key-value mapping) and **Sets** (for managing collections of unique items with mathematical set operations).

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_dict.py` | Introduction to Dictionaries | `student = {"name": "Hamza", "age": 20}` |
| 02 | `02_operation_dict.py` | Dictionary Operations | Accessing keys, modifying values, adding entries |
| 03 | `03_dict_method.py` | Dictionary Methods | `.keys()`, `.values()`, `.items()`, `.get()`, `.update()` |
| 04 | `04_set.py` | Introduction to Sets | `s = {1, 2, 3}`, empty set `s = set()` |
| 05 | `05_set_method.py` | Built-in Set Methods | `.add()`, `.remove()`, `.discard()`, `.clear()` |
| 06 | `06_operation_set.py` | Set Theory Operations | `.union()`, `.intersection()`, `.difference()` |
| 07 | `07_set_comprehension.py` | Set Comprehensions | `{x % 5 for x in range(20)}` |
| 08 | `08_typed_dict.py` | Type-safe Dicts with `TypedDict` | Enforcing dictionary schema for static checkers |
| 10 | `10_dict_comprehension.py` | Dictionary Comprehensions | `{k: v for k, v in zip(keys, vals) if v > 0}` |

---

## 📖 1. Python Dictionaries (`01_dict.py`, `02_operation_dict.py`)

A **dictionary** is an unordered collection of key-value pairs. Keys must be **immutable** and **unique**, while values can be of any data type.

```python
student = {
    "name": "Hamza",
    "course": "Python",
    "marks": 95
}

# Accessing values
print(student["name"])    # 'Hamza'

# Modifying and adding
student["marks"] = 98     # Update existing key
student["city"] = "Mumbai" # Add new key-value pair
```

---

## 🛠️ 2. Dictionary Methods (`03_dict_method.py`)

```python
d = {"a": 1, "b": 2, "c": 3}

print(d.keys())    # dict_keys(['a', 'b', 'c'])
print(d.values())  # dict_values([1, 2, 3])
print(d.items())   # dict_items([('a', 1), ('b', 2), ('c', 3)])

# Safe lookup with .get()
print(d.get("z", "Not Found")) # Returns "Not Found" without crashing!
# print(d["z"])                # ❌ Raises KeyError

# Updating
d.update({"b": 20, "d": 4})
```

---

## ⭕ 3. Sets (`04_set.py`, `05_set_method.py`, `06_operation_set.py`)

A **set** is an unordered collection of **unique, hashable** elements. Duplicates are automatically eliminated.

```python
# Creating sets
numbers = {1, 2, 3, 3, 2, 1}
print(numbers)  # {1, 2, 3} -> duplicates removed!

# Creating an empty set (IMPORTANT)
empty_set = set()      # ✅ Correct
not_a_set = {}         # ❌ This creates an empty DICTIONARY!
```

### Set Operations:
```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1.union(s2))         # {1, 2, 3, 4, 5, 6} (or s1 | s2)
print(s1.intersection(s2))  # {3, 4}             (or s1 & s2)
print(s1.difference(s2))    # {1, 2}             (or s1 - s2)
```

---

## ⚡ 4. Set & Dictionary Comprehensions (`07_set_comprehension.py`, `10_dict_comprehension.py`)

```python
# Set comprehension (unique values only)
unique_lengths = {len(word) for word in ["apple", "banana", "pear", "fig", "kiwi"]}

# Dictionary comprehension
names = ["alice", "bob", "charlie"]
scores = [85, 92, 78]
passed_students = {name.title(): score for name, score in zip(names, scores) if score >= 80}
# {'Alice': 85, 'Bob': 92}
```

---

## 🛡️ 5. `TypedDict` (`08_typed_dict.py`)

From Python's `typing` module, `TypedDict` allows you to declare dictionary shapes with explicit key and value types for static type checking:

```python
from typing import TypedDict

class UserProfile(TypedDict):
    username: str
    age: int
    is_active: bool

user: UserProfile = {
    "username": "hamza_dev",
    "age": 21,
    "is_active": True
}
```

---

## 🎯 Quick Comparison

| Feature | Dictionary (`dict`) | Set (`set`) |
|---|---|---|
| **Structure** | Key-Value pairs (`{k: v}`) | Single elements (`{x}`) |
| **Duplicates** | Keys must be unique | Elements must be unique |
| **Indexing** | By key (`d["key"]`) | No indexing / unindexed |
| **Primary Use** | Lookups, associative records | Deduplication, membership testing, set theory |

---

## 🏋️ Practice Exercises
Test your understanding with 9 practical exercises in **[chapter_05_exercises/](../chapter_05_exercises/README.md)**!

---

## ⏭️ What's Next?
Move on to **[Chapter 06 — Control Flow](../chapter_06/README.md)** to teach your programs how to make decisions!
