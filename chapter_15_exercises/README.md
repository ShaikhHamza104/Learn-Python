# 🐍 Chapter 15 Exercises — Regular Expressions Practice 🔍

Welcome to the **Chapter 15 Practice Exercises**! 🚀  
These 5 exercises focus on essential real-world pattern matching tasks: number extraction, phone number validation, sensitive data masking, vowel word identification, and password security auditing.

---

## 📌 Exercises Overview

| File | Topic | Core Concept | Difficulty |
|---|---|---|---|
| 🔢 [`problem1.py`](./problem1.py) | Extract All Numbers | `re.findall(r"\d+", text)` | 🟢 Beginner |
| 📱 [`problem2.py`](./problem2.py) | Phone Number Validator | `re.fullmatch(r"^[6-9]\d{9}$", phone)` | 🟢 Beginner |
| 🎭 [`problem3.py`](./problem3.py) | Mask Digits in Text | `re.sub(r"\d", "*", text)` | 🟢 Beginner |
| 🔤 [`problem4.py`](./problem4.py) | Words Starting with Vowels | Word boundaries `\b` and character classes `[aeiouAEIOU]` | 🟡 Easy-Medium |
| 🔐 [`problem5.py`](./problem5.py) | Password Strength Validator | Lookahead assertions or multi-pattern matching | 🔴 Medium |

---

## 🔢 Problem 1: Extract Numbers from Text (`problem1.py`)

### ❓ Objective
Write a program that takes a sentence as input and extracts all the numbers from it.

### 💻 Code
```python
import re

text = input("Enter sentence: ")
numbers = re.findall(r"\d+", text)

print("Extracted numbers:", numbers)
```

▶️ **Run:** `python problem1.py`

---

## 📱 Problem 2: Phone Number Validator (`problem2.py`)

### ❓ Objective
Write a program that checks if a 10-digit phone number entered by the user is valid (starting with 6, 7, 8, or 9).

### 💻 Code
```python
import re

phone = input("Enter 10-digit phone number: ").strip()
pattern = r"^[6-9]\d{9}$"

if re.fullmatch(pattern, phone):
    print("✅ Valid Phone Number!")
else:
    print("❌ Invalid Phone Number. Must be 10 digits starting with 6-9.")
```

▶️ **Run:** `python problem2.py`

---

## 🎭 Problem 3: Mask Sensitive Digits (`problem3.py`)

### ❓ Objective
Write a program that hides every digit in a sentence by replacing it with `*`.

### 💻 Code
```python
import re

sentence = input("Enter text containing numbers: ")
masked = re.sub(r"\d", "*", sentence)

print("Masked output:", masked)
```

▶️ **Run:** `python problem3.py`

---

## 🔤 Problem 4: Find Words Starting with Vowels (`problem4.py`)

### ❓ Objective
Write a program that finds all the words in a sentence that start with a vowel (`a, e, i, o, u`).

### 💻 Code
```python
import re

text = input("Enter text: ")
vowel_words = re.findall(r"\b[aeiouAEIOU]\w*", text)

print("Words starting with vowels:", vowel_words)
```

▶️ **Run:** `python problem4.py`

---

## 🔐 Problem 5: Password Strength Validator (`problem5.py`)

### ❓ Objective
Write a program that checks if a password entered by the user is strong:
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character (`@$!%*?&#`)

### 💻 Code
```python
import re

password = input("Enter password to test: ")

is_valid = (
    len(password) >= 8
    and re.search(r"[A-Z]", password)
    and re.search(r"[a-z]", password)
    and re.search(r"\d", password)
    and re.search(r"[@$!%*?&#]", password)
)

if is_valid:
    print("💪 Strong Password!")
else:
    print("⚠️ Weak Password. Ensure it has 8+ characters, uppercase, lowercase, digit, and special char.")
```

▶️ **Run:** `python problem5.py`

---

## ⏭️ What's Next?
Next, discover high-performance specialized data structures in **[Chapter 16 — Collections Module](../chapter_16_collections/README.md)**!
