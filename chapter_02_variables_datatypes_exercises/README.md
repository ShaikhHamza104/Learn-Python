# 📚 Topic: Variables and Data Types Practice (Exercises)

Hands-on practice exercises focusing on Python variables, type conversion, basic arithmetic and comparison operators, terminal user input, and numerical operations.

## 📂 What's in this folder

| File | Description |
|---|---|
| `problem1.py` | Prompts for two integers with `input()` and prints their sum using `+`. |
| `problem2.py` | Demonstrates integer division by calculating `n // z` (floor division) for `n = 37` and `z = 10`. |
| `problem3.py` | Takes user input with `input()`, prints the value, and inspects its type using `type()`. |
| `problem4.py` | Compares two integers (`a = 34`, `b = 80`) using comparison operator `>` to output boolean results. |
| `problem5.py` | Calculates and displays the average of two numbers provided by the user via `(num1 + num2) / 2`. |
| `problem6.py` | Calculates the square of an input integer using `num**2` and `num * num`, noting why `num^2` is bitwise XOR. |

## 💡 Key points

1. **Problem 1 (`problem1.py`)**: `input()` always captures terminal values as strings, requiring explicit type casting with `int()` before arithmetic operations like addition.
2. **Problem 2 (`problem2.py`)**: Demonstrates floor division with `//` to compute the quotient; note that the modulus operator `%` is used when the remainder is desired.
3. **Problem 3 (`problem3.py`)**: Uses `type()` to verify that any raw input captured via `input()` defaults to string type (`<class 'str'>`).
4. **Problem 4 (`problem4.py`)**: Evaluates numeric relationships with comparison operators (`>`), producing boolean values (`True` or `False`).
5. **Problem 5 (`problem5.py`)**: Computes an arithmetic mean using `(num1 + num2) / 2`, relying on parentheses to ensure addition occurs before division.
6. **Problem 6 (`problem6.py`)**: Calculates power using the `**` exponentiation operator or direct multiplication, avoiding the bitwise XOR operator `^`.

## 🧠 Beginner tip

Always watch operator precedence when computing averages or formulas! In Python, `num1 + num2 / 2` evaluates division first according to PEMDAS rules, which only divides `num2`. Grouping the numerator in parentheses `(num1 + num2) / 2` guarantees the addition completes before dividing.

## 📊 Where this is used in Data Science

Data ingestion workflows constantly parse external inputs (CSVs, JSON APIs, databases) where numeric data often arrives as strings. Data engineers and data scientists use explicit type conversions (`int()`, `float()`) and arithmetic aggregations (sums, averages, squares) daily during data validation and feature engineering pipelines.

## 🏃 How to Run Each Exercise

Run each exercise script from your terminal:

```bash
python problem1.py
python problem2.py
python problem3.py
python problem4.py
python problem5.py
python problem6.py
```

## 📖 Related Lessons

- [Chapter 02 - Variables and Data Types](../chapter_02_variables_datatypes/README.md)

## ⏭️ What's Next

- [Chapter 03 - Strings](../chapter_03_strings/README.md)
