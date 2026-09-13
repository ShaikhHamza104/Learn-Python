# 🐍 Chapter 05 Exercises — Dictionaries & Sets Practice 🗝️

Welcome to the **Chapter 05 Practice Exercises**! 🚀  
These 9 problems test your grasp of dictionary lookups, set uniqueness, type coexistence, mutability boundaries, and common traps.

---

## 📌 Exercises Overview

| File | Topic | Core Concept | Difficulty |
|---|---|---|---|
| 📖 [`problem1.py`](./problem1.py) | Hindi-to-English Dictionary | Key-value retrieval with `.get()` | 🟢 Beginner |
| 🔢 [`problem2.py`](./problem2.py) | Unique Numbers Input | Deduplication using `set.add()` | 🟢 Beginner |
| 🔤 [`problem3.py`](./problem3.py) | Integer vs String in Sets | Type differentiation (`18` vs `'18'`) | 🟢 Beginner |
| ⚖️ [`problem4.py`](./problem4.py) | Float & Integer Equality | Numerical equivalence in sets (`20 == 20.0`) | 🟡 Easy-Medium |
| 🏷️ [`problem5.py`](./problem5.py) | Empty Set vs Dict Type | Checking type of `{}` (`type(s) == dict`) | 🟢 Beginner |
| 👥 [`problem6.py`](./problem6.py) | Favorite Languages Dict | Building user-populated dictionaries | 🟢 Beginner |
| 🔄 [`problem7.py`](./problem7.py) | Duplicate Keys in Dict | Key collision & value overwriting | 🟢 Beginner |
| 🔁 [`problem8.py`](./problem8.py) | Duplicate Values in Dict | Multiple keys sharing identical values | 🟢 Beginner |
| 🚫 [`problem9.py`](./problem9.py) | Unhashable Types in Sets | Immutability requirements of set elements | 🟡 Easy-Medium |

---

## 📖 Problem 1: Word Translation Lookup (`problem1.py`)

### ❓ Objective
Create a dictionary of Hindi words with English translations and allow the user to look up a word.

### 💻 Code
```python
oxford = {
    "namaste": "Hello",
    "dost": "Friend",
    "pani": "Water",
    "kitab": "Book"
}

word = input("Enter Hindi word: ").lower()
print("Translation:", oxford.get(word, "Word not found in dictionary!"))
```

### 💡 Key Takeaway
- Always prefer `.get(key, fallback)` over direct square-bracket indexing `dict[key]` to prevent unhandled `KeyError` crashes.

▶️ **Run:** `python problem1.py`

---

## 🔢 Problem 2: Unique Numbers Collector (`problem2.py`)

### ❓ Objective
Input eight numbers from the user and display only unique numbers.

### 💻 Code
```python
unique_numbers = set()

for i in range(1, 9):
    num = int(input(f"Enter number {i}: "))
    unique_numbers.add(num)

print("Unique numbers entered:", unique_numbers)
```

### 💡 Key Takeaway
- Sets automatically drop duplicates as items are inserted via `.add()`.

▶️ **Run:** `python problem2.py`

---

## 🔤 Problem 3: Integer vs. String in Sets (`problem3.py`)

### ❓ Objective
Can you have a set with `18` (integer) and `'18'` (string) as values in it?

### 💻 Code
```python
s = {18, "18"}
print(s)        # {18, '18'}
print(len(s))   # 2
```

### 💡 Key Takeaway
- **Yes!** Python checks both value and type hash. Since `18` is an `int` and `'18'` is a `str`, they are distinct objects in a set.

▶️ **Run:** `python problem3.py`

---

## ⚖️ Problem 4: Set Length with 20 and 20.0 (`problem4.py`)

### ❓ Objective
What will be the length of the following set `s`?
```python
s = set()
s.add(20)
s.add(20.0)
s.add("20")
```

### 💻 Solution & Explanation
```python
print(len(s))  # 2
```
In Python, `20 == 20.0` evaluates to `True`, and both have identical hash values. Thus, `20.0` is treated as a duplicate of `20`. The set only contains `20` (or `20.0`) and `'20'`, making the length **2**.

▶️ **Run:** `python problem4.py`

---

## 🏷️ Problem 5: What is the type of `{}`? (`problem5.py`)

### ❓ Objective
Determine the type of `s = {}`.

### 💻 Code
```python
s = {}
print(type(s))  # <class 'dict'>
```

### 💡 Key Takeaway
- `{}` creates an empty **dictionary**, NOT an empty set. To instantiate an empty set, you must use `set()`.

▶️ **Run:** `python problem5.py`

---

## 👥 Problems 6, 7 & 8: Dictionary Behavior with Keys & Values (`problem6.py`, `problem7.py`, `problem8.py`)

### ❓ Objectives
- **Problem 6**: Create an empty dictionary and allow 4 friends to enter their favorite programming languages.
- **Problem 7**: If the names of 2 friends are the same, what happens?
- **Problem 8**: If the languages of 2 friends are the same, what happens?

### 💡 Key Takeaways
- **Duplicate Keys (Problem 7)**: Keys must be unique. The second entry with the same name **overwrites** the first value.
- **Duplicate Values (Problem 8)**: Values do **not** need to be unique. Two distinct friends can both love `"Python"`.

---

## 🚫 Problem 9: Can you modify a list inside a set? (`problem9.py`)

### ❓ Objective
Can you change the values inside a list which is contained in set `s = {8, 7, 12, "Harry", [1, 2]}`?

### 💡 Key Takeaway
- **No, you cannot!** In fact, Python will not even let you create this set in the first place — it raises `TypeError: unhashable type: 'list'`.
- All elements in a Python set must be **hashable and immutable** (like numbers, strings, and tuples). Lists cannot be placed inside sets.

---

## ⏭️ What's Next?
Next, master conditional decision making in **[Chapter 06 — Control Flow](../chapter_06/README.md)**!
