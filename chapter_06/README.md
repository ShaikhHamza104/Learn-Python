# 🐍 Chapter 06 — Control Flow: Making Decisions in Python 🔀

Welcome to Chapter 6! Until now, your programs executed sequentially from top to bottom. With **Control Flow**, you give your programs the ability to evaluate conditions, make decisions, and execute different branches of code dynamically.

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_if.py` | The Simple `if` Statement | `if age >= 18: print("Eligible to vote")` |
| 02 | `02_if_else.py` | Two-way Decisions with `if-else` | Binary decision branch |
| 03 | `03_if_elif_else.py` | Multi-way Ladders | Evaluating multiple mutually exclusive conditions |
| 04 | `04_short_hand_if_else.py` | Ternary / Short-hand `if-else` | `status = "Adult" if age >= 18 else "Minor"` |
| 05 | `05_calculator.py` | Practical Application: Calculator | Menu-driven arithmetic calculator |
| 06 | `06_leap_year.py` | Leap Year Algorithm | Compound boolean logic with `and`, `or` |
| 07 | `07_multiple_if.py` | Independent vs Chained `if` | When to use separate `if` blocks vs `elif` |

---

## 🚦 1. The `if`, `elif`, and `else` Ladder (`01_if.py`, `02_if_else.py`, `03_if_elif_else.py`)

Python uses 4-space indentation to define blocks of code that execute conditionally.

```python
score = 82

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # This runs!
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

> [!IMPORTANT]
> In an `if-elif-else` chain, Python stops evaluating as soon as it encounters the **first `True` condition**.

---

## ⚡ 2. Short-Hand / Ternary Operator (`04_short_hand_if_else.py`)

For compact assignments based on conditions, use Python's ternary conditional expression:

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult
```

---

## 🧮 3. Building Practical Logic (`05_calculator.py`, `06_leap_year.py`)

### Leap Year Rules:
A year is a leap year if:
1. It is divisible by 4, **AND**
2. Not divisible by 100, **UNLESS** it is also divisible by 400.

```python
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year!")
else:
    print(f"{year} is NOT a Leap Year.")
```

---

## ⚖️ 4. Multiple Independent `if` vs `elif` (`07_multiple_if.py`)

```python
age = 25

# Independent if statements: ALL conditions are checked
if age > 10:
    print("Greater than 10")  # Runs
if age > 20:
    print("Greater than 20")  # Runs too!

# elif chain: Only ONE block runs
if age > 10:
    print("Greater than 10")  # Runs
elif age > 20:
    print("Greater than 20")  # Skipped!
```

---

## 🏋️ Practice Exercises
Ready to test your conditional logic? Work through the 7 real-world challenges in **[chapter_06_exercises/](../chapter_06_exercises/README.md)**!

---

## ⏭️ What's Next?
Now learn how to repeat actions effortlessly in **[Chapter 07 — Loops](../chapter_07/README.md)**!
