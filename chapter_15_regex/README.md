# 🐍 Chapter 15 — Regular Expressions (Regex): Pattern Matching 🔍

Welcome to Chapter 15! Regular expressions (regex) provide a concise, powerful language for searching, matching, extracting, and modifying text patterns. From validating email addresses and phone numbers to scraping data and sanitizing inputs, Python's built-in `re` module is an indispensable tool in any developer's toolkit.

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_intro_re.py` | Introduction to `re` | `re.match()`, `re.search()`, and `re.findall()` |
| 02 | `02_groups_and_substitution.py` | Groups and Substitution | Capturing `()` and string replacement with `re.sub()` |
| 03 | `03_common_patterns.py` | Real-World Regex Patterns | Email, phone, date validation with `re.fullmatch()` |

---

## 🔍 1. Match, Search, and Findall (`01_intro_re.py`)

Python's `re` module offers three primary functions to locate patterns:

| Method | Behavior | Returns |
|---|---|---|
| `re.match(pattern, string)` | Looks for a match **only at the beginning** of the string | `Match` object or `None` |
| `re.search(pattern, string)` | Scans through the entire string for the **first match** | `Match` object or `None` |
| `re.findall(pattern, string)` | Finds **all non-overlapping matches** across the string | `list` of strings |

```python
import re

text = "Hamza is learning Python in 2026. Python is awesome!"

# re.search scans anywhere in text
match = re.search(r"Python", text)
if match:
    print("Found:", match.group())       # 'Python'
    print("Start position:", match.start()) # Index where match begins

# re.findall extracts all occurrences
words = re.findall(r"Python", text)
print("Occurrences:", words)            # ['Python', 'Python']

# Extracting all numbers
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)        # ['2026']
```

---

## ✂️ 2. Capturing Groups & Substitution (`02_groups_and_substitution.py`)

Parentheses `()` define **capturing groups**, allowing you to extract individual segments of a matched pattern:

```python
import re

date_text = "Today is 11-09-2026"
match = re.search(r"(\d{2})-(\d{2})-(\d{4})", date_text)

if match:
    day, month, year = match.groups()
    print(f"Day: {day}, Month: {month}, Year: {year}")

# Substitution with re.sub(pattern, replacement, string)
cleaned_text = re.sub(r"\d", "*", "Order ID: 98765")
print(cleaned_text)  # "Order ID: *****"
```

---

## 🎯 3. Practical Validation Patterns (`03_common_patterns.py`)

Using `re.fullmatch(pattern, string)` ensures the **entire** string conforms to the expected format:

```python
import re

# Email validation pattern
email_pattern = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"
print(bool(re.fullmatch(email_pattern, "hamza@gmail.com")))  # True
print(bool(re.fullmatch(email_pattern, "invalid-email")))    # False

# 10-digit Phone number pattern (India: starts with 6, 7, 8, or 9)
phone_pattern = r"^[6-9]\d{9}$"
print(bool(re.fullmatch(phone_pattern, "9876543210")))       # True
```

---

## 🏋️ Practice Exercises
Put your regex skills into practice across 5 real-world validation problems in **[chapter_15_exercises/](../chapter_15_exercises/README.md)**!

---

## ⏭️ What's Next?
Next, discover specialized container data types in **[Chapter 16 — Collections Module](../chapter_16_collections/README.md)**!
