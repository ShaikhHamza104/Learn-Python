# 📚 Topic: Dictionaries & Sets

Python dictionaries and sets are high-performance data structures engineered for instant lookups and organized data storage. A dictionary pairs a unique **key** with a **value** (like looking up an employee ID to find a name), while a set holds an unordered group of strictly **unique elements** with no duplicates. Both structures exist so your programs can search, update, and deduplicate information in constant time without scanning sequentially through an entire list.

---

## 📂 What's in this folder

| File | What it teaches |
|------|------------------|
| `01_dict.py` | Creating dictionaries with key-value pairs and inspecting their data type with `type()`. |
| `02_operation_dict.py` | Accessing dictionary values by key, reassigning values, and adding new entries. |
| `03_dict_method.py` | Working with dictionary methods like `.keys()`, `.values()`, `.items()`, and crash-safe `.get()`. |
| `04_set.py` | Initializing sets, checking membership, and creating an empty set using `set()` rather than `{}`. |
| `05_set_method.py` | Adding and removing set items using `.add()`, `.remove()`, and `.discard()`. |
| `06_operation_set.py` | Performing mathematical set operations: union (`|`), intersection (`&`), and difference (`-`). |
| `07_set_comprehension.py` | Generating and transforming sets concisely using set comprehension syntax. |
| `08_typed_dict.py` | Defining rigid dictionary schemas and type contracts using Python's `TypedDict`. |
| `09_dict_comprehension.py` | Constructing and filtering new dictionaries dynamically with dictionary comprehensions. |

---

## 💡 Key points

1. **Keys and set items must be hashable**: Dictionary keys and set elements must be immutable data types (such as strings, integers, or tuples) so Python can look them up instantly.
2. **Sets automatically eliminate duplicates**: Adding the same element to a set multiple times retains only one copy, making sets ideal for finding distinct values.
3. **Use `.get()` for defensive programming**: Accessing a missing key via `dict[key]` raises a fatal `KeyError`, whereas `dict.get(key, default)` returns a safe default value if the key does not exist.

---

## 🧠 Beginner tip

Remember that `{}` always creates an empty dictionary in Python, never an empty set! If you need an empty set, always write `empty_set = set()`.

---

## 📊 Where this is used in Data Science

Dictionaries are used constantly in data science for parsing nested JSON records from REST APIs, configuring model parameters (such as `{"learning_rate": 0.01, "max_depth": 5}`), and mapping categorical labels to integers before feeding data into Scikit-learn or PyTorch models. Sets are the industry standard for feature comparison across training and test splits—for instance, quickly checking if a test dataset contains unseen categorical values via `set(test_categories) - set(train_categories)`.

---

## 🛠️ Code Examples & Quick Comparison

### Dictionary Basics (`01_dict.py`, `02_operation_dict.py`, `03_dict_method.py`)
```python
# Create a dictionary
student = {"name": "Hamza", "marks": 95}

# Safe lookup with .get()
print(student.get("name", "Unknown"))   # "Hamza"
print(student.get("grade", "Not set"))  # "Not set" (does not crash!)

# Iterate over keys and values
for key, val in student.items():
    print(f"{key} -> {val}")
```

### Set Operations (`04_set.py`, `05_set_method.py`, `06_operation_set.py`)
```python
# Duplicates are automatically dropped
nums = {1, 2, 2, 3, 4, 4}
print(nums)  # {1, 2, 3, 4}

# Set theory operations
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))         # {1, 2, 3, 4, 5}
print(s1.intersection(s2))  # {3}
print(s1.difference(s2))    # {1, 2}
```

### Comprehensions & TypedDict (`07_set_comprehension.py`, `08_typed_dict.py`, `09_dict_comprehension.py`)
```python
from typing import TypedDict

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# TypedDict schema definition
class StudentRecord(TypedDict):
    name: str
    score: float

record: StudentRecord = {"name": "Aria", "score": 92.5}
```

---

## 🏋️ Practice Exercises
Ready to test your knowledge? Work through the 9 practical challenges in **[chapter_05_dicts_sets_exercises/](../chapter_05_dicts_sets_exercises/README.md)**!

---

## ⏭️ What's Next?
Now that you can manage collections and mappings, head to **[Chapter 06 — Control Flow](../chapter_06_control_flow/README.md)** to teach your programs how to make conditional decisions!
