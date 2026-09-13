# 📚 Topic: Variables, Data Types & Operators

Variables are named storage containers in memory that allow your program to hold, update, and manipulate data during execution. Python is dynamically typed, meaning it automatically recognizes whether you are storing text, whole numbers, decimals, or truth values without requiring explicit type declarations. This chapter covers variable naming conventions, core data types, arithmetic and logical operators, type casting, and reading user input from the console.

---

## 📂 What's in this folder

| File | What it teaches |
|------|------------------|
| `01_variable.py` | Declaring variables and storing different types of data (integers, floats, strings, booleans, and `None`). |
| `02_datatype.py` | Exploring fundamental Python data types (`int`, `float`, `str`, `bool`, `NoneType`) and inspecting them with `type()`. |
| `03_ruleofvariable.py` | Python identifier naming rules (allowed characters, capitalization conventions, and reserved keyword restrictions). |
| `04_operator.py` | Working with arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`), comparison, logical, and assignment operators. |
| `05_type_function.py` | Using the built-in `type()` function to inspect the runtime class of variables. |
| `06_type_casting.py` | Explicitly converting between data types using constructor functions like `int()`, `float()`, and `str()`. |
| `07_input.py` | Capturing interactive user input using `input()` and processing input strings. |

---

## 💡 Key points

1. **Dynamic typing**: You do not declare variable types explicitly in Python; variable types are inferred when values are assigned and can change dynamically.
2. **`input()` always returns a string**: Regardless of what the user types (even digits like `42`), `input()` produces a `str`; you must explicitly cast to `int()` or `float()` to do math.
3. **Division differences**: Normal division (`/`) always returns a floating-point number (e.g., `4 / 2` is `2.0`), while floor division (`//`) discards the fractional part and returns an integer.

---

## 🧠 Beginner tip

Watch out for string concatenation! If `a = input("Enter a: ")` is `5` and `b = input("Enter b: ")` is `10`, `a + b` will produce `"510"`, not `15`. Always wrap your inputs in `int()` or `float()` when expecting numerical values: `a = int(input("Enter a: "))`.

---

## 📊 Where this is used in Data Science

Data types and type casting are critical during the data ingestion and exploratory data analysis (EDA) stages. When loading messy CSV files or SQL query results into Pandas DataFrames, numeric columns with missing values or currency symbols often load as generic text (`object` type). Data scientists constantly inspect data types (`df.dtypes`) and perform type conversions (`df['revenue'].astype(float)`) before running statistical calculations, plotting distributions, or feeding feature matrices into machine learning algorithms.

---

## 🛠️ Code Examples

### 1. Variables and Data Types (`01_variable.py`, `02_datatype.py`)
```python
age = 21             # Integer (int)
gpa = 3.85           # Floating point (float)
name = "Hamza"       # String (str)
is_student = True    # Boolean (bool)
profile = None       # NoneType (absence of value)

print(type(age))     # <class 'int'>
print(type(gpa))     # <class 'float'>
```

### 2. Operators & Arithmetic (`04_operator.py`)
```python
a = 15
b = 4

print("Sum:", a + b)           # 19
print("Float Division:", a / b) # 3.75
print("Floor Division:", a // b)# 3
print("Modulus (Remainder):", a % b) # 3
print("Exponent (Power):", a ** 2)   # 225
```

### 3. Type Casting (`06_type_casting.py`)
```python
str_num = "100"
converted_int = int(str_num)      # Converts "100" -> 100
converted_float = float(str_num)  # Converts "100" -> 100.0

pi = 3.14159
int_pi = int(pi)                  # Truncates to 3
```

### 4. Reading User Input (`07_input.py`)
```python
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"Hello {user_name}, next year you will be {user_age + 1}!")
```

---

## 🏋️ Practice Exercises
Ready to test your understanding of variables, math, and inputs? Try the 6 hands-on problems in **[chapter_02_variables_datatypes_exercises/](../chapter_02_variables_datatypes_exercises/README.md)**!

---

## ⏭️ What's Next?
Now that you can store numbers and values, head over to **[Chapter 03 — Strings](../chapter_03_strings/README.md)** to master string slicing, formatting, and text manipulation methods!
