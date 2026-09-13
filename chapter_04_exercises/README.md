# 🐍 Chapter 04 Exercises — Lists & Tuples Practice 📋

Welcome to the **Chapter 04 Practice Exercises**! 🚀  
These exercises test your ability to collect user input into lists, perform sorting operations, verify the immutability of tuples, calculate sums, and use tuple methods like `.count()`.

---

## 📌 Exercises Overview

| File | Topic | Key Concept | Difficulty |
| :--- | :--- | :--- | :--- |
| 🍎 [`problem1.py`](./problem1.py) | Store User Input in a List | Adding 5 items to a list using `.append()` | 🟢 Beginner |
| 📊 [`problem2.py`](./problem2.py) | Student Marks Sorter | Collecting numeric marks and sorting them with `.sort()` | 🟢 Beginner |
| 🔒 [`problem3.py`](./problem3.py) | Tuple Immutability | Demonstrating that tuples cannot be altered (`TypeError`) | 🟢 Beginner |
| ➕ [`problem4.py`](./problem4.py) | Sum of List Numbers | Summing numeric elements using `sum()` | 🟢 Beginner |
| 🔢 [`problem5.py`](./problem5.py) | Count Zeros in a Tuple | Counting occurrences using `tuple.count()` | 🟢 Beginner |

---

## 🍎 Problem 1: Seven / Five Fruits in a List (`problem1.py`)

### ❓ Objective
Write a program to store five fruit names entered by the user in a list.

### 💻 Code
```python
fruits = []

for i in range(1, 6):
    fruit = input(f"Enter Fruit {i} name: ")
    fruits.append(fruit)

print("Fruits list:", fruits)
```

### 💡 Key Takeaway
- Lists grow dynamically — each `.append()` adds an element to the end.
- User input via `input()` can be directly passed into list methods.

▶️ **Run:** `python problem1.py`

---

## 📊 Problem 2: Sort Student Marks (`problem2.py`)

### ❓ Objective
Write a program to accept marks of 6 students and display them in a sorted manner.

### 💻 Code
```python
marks = []

for i in range(1, 7):
    mark = int(input(f"Enter marks for student {i}: "))
    marks.append(mark)

# Sort in ascending order
marks.sort()
print("Sorted marks:", marks)
```

### 💡 Key Takeaway
- Use `int()` to convert string inputs into numbers before sorting.
- `.sort()` rearranges the list in place in ascending order.

▶️ **Run:** `python problem2.py`

---

## 🔒 Problem 3: Check Tuple Immutability (`problem3.py`)

### ❓ Objective
Check that a tuple type cannot be changed in Python.

### 💻 Code
```python
t = (1, 2, 3, True, None)

# Attempting to reassign an element:
# t[0] = 90  # ❌ Raises TypeError: 'tuple' object does not support item assignment
```

### 💡 Key Takeaway
- Tuples are **immutable**. Once created, their items cannot be modified, replaced, or deleted.
- Use tuples whenever you want to protect data from accidental modification.

▶️ **Run:** `python problem3.py`

---

## ➕ Problem 4: Sum of a List (`problem4.py`)

### ❓ Objective
Write a program to sum a list with 4 numbers.

### 💻 Code
```python
li = [22, 27, 98, 89]
total = sum(li)
print("Total sum:", total)  # 236
```

### 💡 Key Takeaway
- Python's built-in `sum()` function efficiently adds up all items in any numeric iterable.

▶️ **Run:** `python problem4.py`

---

## 🔢 Problem 5: Count Number of Zeros (`problem5.py`)

### ❓ Objective
Write a program to count the number of zeros in the tuple `(7, 0, 8, 0, 0, 9)`.

### 💻 Code
```python
a = (7, 0, 8, 0, 0, 9)
count = a.count(0)
print("Number of zeros:", count)  # 3
```

### 💡 Key Takeaway
- `tuple.count(x)` searches through the tuple and returns the exact number of times `x` occurs.

▶️ **Run:** `python problem5.py`

---

## 🎯 Quick Recap

| Function / Method | Example | Action |
|---|---|---|
| `list.append(x)` | `li.append("apple")` | Adds `x` to the end of the list |
| `list.sort()` | `li.sort()` | Sorts items in ascending order in place |
| `sum(iterable)` | `sum([1, 2, 3])` | Returns arithmetic total (6) |
| `tuple.count(x)` | `(0, 1, 0).count(0)` | Counts occurrences of `x` (2) |

---

## ⏭️ What's Next?
Now let's explore key-value mappings and unordered unique collections in **[Chapter 05 — Dictionaries & Sets](../chapter_05/README.md)**!
