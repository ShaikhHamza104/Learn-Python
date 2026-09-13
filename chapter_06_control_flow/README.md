# 📚 Topic: Control Flow

Control flow structures allow Python programs to make decisions and execute specific blocks of code based on dynamic conditions. This chapter covers fundamental conditional statements including single-branch `if`, two-way `if-else` branching, multi-branch `if-elif-else` ladders, one-line short-hand ternary expressions, arithmetic operator evaluation in an interactive calculator, nested leap year calendar logic, and tiered fee calculation combining nested conditionals with independent add-on checks.

## 📂 What's in this folder

| File | What it teaches |
|---|---|
| `01_if.py` | Basic single-branch `if` statement evaluating whether an entered age is under 18. |
| `02_if_else.py` | Two-way branching with `if-else` to determine voting eligibility based on age. |
| `03_if_elif_else.py` | Multi-branch ladder checking invalid age input (`<= 0`), minors (`< 18`), and eligible voters (`else`). |
| `04_short_hand_if_else.py` | Compact one-line ternary conditional expression (`print(a) if a > b else print(b)`). |
| `05_calculator.py` | Interactive terminal calculator routing arithmetic operators (`+`, `-`, `*`, `/`) using an `if-elif-else` structure. |
| `06_leap_year.py` | Nested conditional algorithm verifying leap-year divisibility rules (`year % 4`, `year % 100`, and `year % 400`). |
| `07_multiple_if.py` | Rollercoaster billing program demonstrating nested tier pricing based on age and an independent `if` check for optional photo fees. |

## 💡 Key points

1. **Sequential Evaluation**: In an `if-elif-else` ladder, Python evaluates conditions from top to bottom and runs only the first branch that evaluates to `True`.
2. **Indentation Rules**: Python relies on 4-space indentation to define the code block belonging to each conditional branch.
3. **Ternary Expressions**: Short-hand `if-else` expressions (`<expr1> if <condition> else <expr2>`) provide a clean syntax for inline assignments and evaluations.
4. **Nested vs. Independent `if`s**: Nested `if` statements evaluate only when parent conditions pass, whereas independent `if` statements evaluate sequentially to accumulate results (such as optional add-on fees).
5. **Divisibility with Modulus**: The modulus operator (`%`) evaluates remainders; testing `% divisor == 0` is the standard approach for checking divisibility in algorithms like leap year calculation.

## 🧠 Beginner tip

Mind the ordering of your conditions in `if-elif-else` ladders! Always place specific or boundary conditions first (e.g., checking `age <= 0` before `age < 18`). If a broad condition is placed earlier in the ladder, it will capture input prematurely and prevent more specific subsequent checks from running.

## 📊 Where this is used in Data Science

Conditional logic is fundamental to data processing, categorization, and rule-based feature engineering. Data scientists use conditional branching to flag invalid measurements, categorize continuous variables into discrete buckets (e.g., age brackets or risk tiers), handle null values, and apply vectorized conditions using Pandas (`np.where()`, `df.apply()`).

## 🛠️ Code Examples

### If-Elif-Else Ladder (`03_if_elif_else.py`)
```python
age = int(input("Enter your age: "))
if age <= 0:
    print("Your age is invalid.....")
elif age < 18:
    print("You cannot vote")
else:
    print("You can vote")
```

### Short-Hand Ternary Operator (`04_short_hand_if_else.py`)
```python
a = int(input("Enter number: "))
b = int(input("Enter number: "))
print(a) if a > b else print(b)
```

### Operator Routing (`05_calculator.py`)
```python
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid operator!")
```

### Nested & Independent Conditions (`07_multiple_if.py`)
```python
height = int(input("Enter height in cm: "))
bill = 0

if height >= 120:
    age = int(input("Enter age: "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12

    photo = input("Do you want a photo? ")
    if photo in ("yes", "y"):
        bill += 3

    print(f"Total bill: ${bill}")
else:
    print("Cannot ride")
```

## 🏋️ Practice Exercises

Sharpen your conditional logic skills with the practice exercises:
- [Chapter 06 Exercises](../chapter_06_control_flow_exercises/README.md)

## ⏭️ What's Next

- [Chapter 07 - Loops](../chapter_07_loops/README.md)
