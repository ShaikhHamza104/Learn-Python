# 🐍 Chapter 06 Exercises — Control Flow Practice 🔀

Welcome to the **Chapter 06 Practice Exercises**! 🚀  
These 7 problems help you master conditional logic, compound boolean statements with `and`/`or`, string searches, and real-world classification algorithms.

---

## 📌 Exercises Overview

| File | Topic | Core Logic | Difficulty |
|---|---|---|---|
| 🏆 [`problem1.py`](./problem1.py) | Greatest of 4 Numbers | Multi-branch comparison logic | 🟢 Beginner |
| 🎓 [`problem2.py`](./problem2.py) | Pass / Fail Percentage | Dual condition (`total >= 40%` and `each >= 33%`) | 🟡 Easy-Medium |
| 🛡️ [`problem3.py`](./problem3.py) | Spam Comment Filter | Keyword membership testing with `in` | 🟢 Beginner |
| 👤 [`problem4.py`](./problem4.py) | Username Length Validation | Measuring length with `len(username) < 10` | 🟢 Beginner |
| 📋 [`problem5.py`](./problem5.py) | Name Presence in List | Sequence membership check (`name in user_list`) | 🟢 Beginner |
| 📊 [`problem6.py`](./problem6.py) | Marks to Grade Converter | Multi-level `if-elif-else` grading scale | 🟢 Beginner |
| 🔍 [`problem7.py`](./problem7.py) | Topic Mentions in Posts | Case-insensitive substring matching (`in post.lower()`) | 🟢 Beginner |

---

## 🏆 Problem 1: Greatest of Four Numbers (`problem1.py`)

### ❓ Objective
Write a program to find the greatest of four numbers entered by the user.

### 💻 Code
```python
a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))
c = int(input("Enter num 3: "))
d = int(input("Enter num 4: "))

if a >= b and a >= c and a >= d:
    greatest = a
elif b >= c and b >= d:
    greatest = b
elif c >= d:
    greatest = c
else:
    greatest = d

print("The greatest number is:", greatest)
```

▶️ **Run:** `python problem1.py`

---

## 🎓 Problem 2: Pass/Fail Evaluation (`problem2.py`)

### ❓ Objective
Write a program to determine if a student has passed or failed. To pass, the student requires a total of at least 40% overall and at least 33% in each of the three subjects.

### 💻 Code
```python
sub1 = int(input("Enter Marks for Subject 1: "))
sub2 = int(input("Enter Marks for Subject 2: "))
sub3 = int(input("Enter Marks for Subject 3: "))

total_percentage = (sub1 + sub2 + sub3) / 3

if total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print(f"Passed! Overall Percentage: {total_percentage:.2f}%")
else:
    print(f"Failed! Overall Percentage: {total_percentage:.2f}%")
```

▶️ **Run:** `python problem2.py`

---

## 🛡️ Problem 3: Spam Comment Detector (`problem3.py`)

### ❓ Objective
A spam comment is defined as containing text such as:
- "make a lot of money"
- "buy now"
- "subscribe this"
- "click this"

Write a program to detect these spam phrases.

### 💻 Code
```python
spam_phrases = ["make a lot of money", "buy now", "subscribe this", "click this"]
comment = input("Enter comment: ").lower()

is_spam = any(phrase in comment for phrase in spam_phrases)

if is_spam:
    print("⚠️ Spam detected!")
else:
    print("✅ Safe comment.")
```

▶️ **Run:** `python problem3.py`

---

## 👤 Problem 4: Username Character Counter (`problem4.py`)

### ❓ Objective
Write a program to check whether a given username contains less than 10 characters.

### 💻 Code
```python
username = input("Enter username: ")

if len(username) < 10:
    print("Username is less than 10 characters.")
else:
    print("Username is 10 or more characters.")
```

▶️ **Run:** `python problem4.py`

---

## 📋 Problem 5: Name in List Checker (`problem5.py`)

### ❓ Objective
Write a program to check whether a given name is present in a list of names.

### 💻 Code
```python
registered_users = ["hamza", "ali", "sara", "harry", "john"]
name = input("Enter name to search: ").lower()

if name in registered_users:
    print(f"'{name}' is present in the list.")
else:
    print(f"'{name}' was not found.")
```

▶️ **Run:** `python problem5.py`

---

## 📊 Problem 6: Marks to Grade Scheme (`problem6.py`)

### ❓ Objective
Calculate student grade according to:
- 90–100 → `Ex`
- 80–90 → `A`
- 70–80 → `B`
- 60–70 → `C`
- 50–60 → `D`
- < 50 → `F`

### 💻 Code
```python
marks = int(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "Ex"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Assigned Grade:", grade)
```

▶️ **Run:** `python problem6.py`

---

## 🔍 Problem 7: Detecting Post Mentions (`problem7.py`)

### ❓ Objective
Write a program to find out whether a given social media post is talking about "Harry" or not.

### 💻 Code
```python
post = input("Enter post text: ")

if "harry" in post.lower():
    print("This post is talking about Harry.")
else:
    print("This post does not mention Harry.")
```

▶️ **Run:** `python problem7.py`

---

## ⏭️ What's Next?
Let's automate repetition! Move on to **[Chapter 07 — Loops](../chapter_07/README.md)**!
