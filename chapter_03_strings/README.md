# 📚 Topic: Strings

Strings are immutable sequences of characters used for representing and working with textual data in Python. This chapter covers string declaration across single, double, and triple quotes, character indexing, slicing with step strides, essential string manipulation methods, string interpolation with f-strings, and escape sequences.

## 📂 What's in this folder

| File | What it teaches |
|---|---|
| `01_intro_string.py` | String declaration (single, double, multi-line triple quotes) and positive vs. negative character indexing. |
| `02_slicing.py` | Substring slicing syntax using `[start:end]` and step intervals with `[start:end:step]`. |
| `03_negative_slicing.py` | Slicing strings using negative index boundaries (`name[-4:-1]`, `name[-2:-1]`). |
| `04_string_method.py` | Common string methods: `len()`, `.upper()`, `.lower()`, `.capitalize()`, `.title()`, `.find()`, `.count()`, `.isalpha()`, `.isdigit()`, `.replace()`, `.strip()`, and `.split()`. |
| `05_formatting_strings.py` | String interpolation techniques including `%` formatting, `.format()`, and modern f-strings (`f"{name}"`). |
| `06_escape.py` | Working with nested quotes and escape sequences such as newline (`\n`). |

## 💡 Key points

1. **Immutability**: Python strings cannot be modified in-place; all string operations and methods return new string objects.
2. **Indexing Boundaries**: Positive indices count forward starting at `0`, while negative indices count backward starting from the end at `-1`.
3. **Exclusive Slice End**: Slicing with `[start:end]` includes `start` but excludes `end`.
4. **Step Parameter**: In `[start:end:step]`, the step argument determines the character jump interval across the string.
5. **String Methods**: Methods like `.strip()`, `.lower()`, and `.split()` provide clean, expressive ways to sanitize and break down text.
6. **Modern Formatting**: F-strings (`f"..."`) are the standard, readable, and performant approach for injecting variables and expressions into strings.

## 🧠 Beginner tip

Remember that the stop index in string slicing is always non-inclusive (exclusive)! For example, `"Hamza"[0:3]` extracts indices 0, 1, and 2 (`"Ham"`), leaving out index 3.

## 📊 Where this is used in Data Science

Text cleaning and preprocessing are essential steps in Natural Language Processing (NLP) and exploratory data analysis. Data scientists routinely clean messy column values in Pandas using string methods (`.strip()`, `.lower()`, `.replace()`), tokenize raw text with `.split()`, and format output summaries and log metrics with f-strings.

## 🛠️ Code Examples

### String Creation and Indexing (`01_intro_string.py`)
```python
name = "Hamza"
print(name[0])   # First character: 'H'
print(name[-1])  # Last character: 'a'
```

### Forward & Negative Slicing (`02_slicing.py`, `03_negative_slicing.py`)
```python
word = "Amazing"
print(word[0:3])    # 'Ama'
print(word[1:6:3])  # 'mi' (step by 3)
print(word[-4:-1])  # 'zin'
```

### String Methods (`04_string_method.py`)
```python
s = "  Python programming  "
cleaned = s.strip().title()  # "Python Programming"
words = cleaned.split()      # ['Python', 'Programming']
print(cleaned.replace("Python", "Data"))
```

### Formatting & Escape Sequences (`05_formatting_strings.py`, `06_escape.py`)
```python
name, age = "Hamza", 18
print(f"The name of student is {name} and age is {age}")
print("He said, 'I am learning Python.'\nWelcome!")
```

## 🏋️ Practice Exercises

Sharpen your string manipulation skills with the exercises in the practice folder:
- [Chapter 03 Exercises](../chapter_03_strings_exercises/README.md)

## ⏭️ What's Next

- [Chapter 04 - Lists and Tuples](../chapter_04_lists_tuples/README.md)
