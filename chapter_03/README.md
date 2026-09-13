# Chapter 3: Strings – Sculpting Text in Python 📜

Welcome to Chapter 3! If variables and data types were your program’s memory, then strings are its voice and handwriting. In this chapter, you’ll learn how to create, inspect, transform, and format text—everything from grabbing a single character to crafting complex messages.

By the end of this chapter, you’ll be able to:
- Create strings with single, double, and triple quotes
- Access characters by positive and negative indexes
- Slice text into substrings—simple and with steps
- Use Python’s powerful string methods (uppercase, find, replace, split, and more)
- Format messages using `%`, `.format()`, and f-strings
- Handle special characters with escape sequences

## 📂 Files in This Chapter

| File                        | Topic                         | Quick Peek                                           |
|-----------------------------|-------------------------------|------------------------------------------------------|
| `01_intro_string.py`        | String creation & indexing    | `'Hello'`, `"Hello"`, `'''Hello'''`, `name[0]`      |
| `02_slicing.py`             | Basic slicing                 | `text[1:4]`, `text[:3]`, `text[::2]`                  |
| `03_negative_slicing.py`    | Slicing with negative indexes | `text[-4:-1]`, `text[-2:]`                            |
| `04_string_method.py`       | String methods                | `len()`, `.upper()`, `.replace()`, `.split()`, etc.  |
| `05_formatting_strings.py`   | Formatting                     | `%s`, `.format()`, `f"..."`                        |
| `06_escape.py`              | Escape sequences              | `\n`, `\'`, `\"`                                  |

---

## 1. `01_intro_string.py` – Your First Glance at Strings

```python
# Single quotes
string = 'This is a string'

# Double quotes
string = "This is also a string"

# Triple quotes for multi-line text
string = '''This
is
a
multi-line string'''

name = "Hamza"
# Positive indexing: first character is index 0
print(name[0])  # H
print(name[3])  # z

# Negative indexing: last character is -1
print(name[-1]) # a
print(name[-2]) # z
```

### What’s happening?
- **Quotes matter**: single `'`, double `"`, and triple `'''` each create string literals.
- **Indexing**: `name[0]` → first character, `name[-1]` → last character.
- Strings in Python are **immutable**: you can read characters, but not change them in place.

### Try It Yourself:
1. Print the middle letter of your name: `name[len(name)//2]`.
2. Combine quotes: `'He said, "Hello"'` and print it.
3. Experiment with a three-quoted string that preserves line breaks.

---

## 2. `02_slicing.py` – Cutting Out Substrings

```python
word = "Amazing"
#     0123456
# Basic slice: [start:end]
print(word[0:3])    # Ama
print(word[1:4])    # maz
print(word[:3])     # Ama (from start)
print(word[3:])     # zing (to end)
print(word[:])      # Amazing (whole string)

# Extended slice: [start:end:step]
print(word[0:7:2])  # Aazi (every 2nd char)
print(word[1:6:3])  # mi  (positions 1 and 4)
```

### The Power of Slicing
- **`start`** and **`end`** define the substring boundaries (end is exclusive).
- **`step`** lets you skip characters (e.g. `::2` picks every other character).
- Omitting **start** or **end** defaults to the beginning or end of the string.

### Hands-On Challenges:
- Reverse a string using slicing: `word[::-1]`.
- Extract every third character: `word[::3]`.
- Write a function `middle(text)` that returns exactly the middle two characters when the length is even.

---

## 3. `03_negative_slicing.py` – Slicing with Negative Indexes

```python
name = "Hamza"
#     012345
print(name[-4:-1])  # amz  (from -4 up to but not including -1)
print(name[-3:])    # mza  (last 3 characters)
```

### Why Negative Slices?
- Negative indexes count from the **end** of the string.
- Combine negative start/end to grab substrings relative to the tail.

### Experiment:
- Grab the last four letters of any sentence you like.
- Use slicing to remove the first and last character: `text[1:-1]`.

---

## 4. `04_string_method.py` – Python’s String Toolbox

```python
name = "hamza"
print(len(name))             # 5
print(name.startswith("ha"))# False (case matters)
print(name.endswith("za"))  # True
print(name.upper())           # HAMZA
print(name.capitalize())      # Hamza
print(name.find("a"))       # 1 (first occurrence)
print(name.count("a"))      # 2
print(name.replace("h","H"))  # Hamza

s = "   Python   "
print(s.strip())              # "Python" (no extra spaces)

s2 = "Hello world"
print(s2.split())             # ['Hello', 'world']
print(s2.title())             # "Hello World"
```

### Top Methods to Know:
- **`len()`**: length of the string
- **`.upper()`, `.lower()`, `.capitalize()`, `.title()`**: change case
- **`.find()`, `.count()`, `.replace()`**: search & modify
- **`.strip()`, `.split()`**: clean and split text
- **`.startswith()`, `.endswith()`**: quick checks

### Practice:
- Normalize user input: `text.strip().lower()`.
- Mask a password: replace all but last 2 characters with `*`.
- Check if a sentence is a palindrome ignoring spaces and case.

---

## 5. `05_formatting_strings.py` – Making Messages Dynamic

```python
name = "Hamza"
age = 18

# 1. %-formatting (old style)
print("Student: %s, Age: %d" % (name, age))

# 2. str.format()
print("Student: {}, Age: {}".format(name, age))

# 3. f-strings (Python 3.6+)
print(f"Student: {name}, Age: {age}")
```

### When to Use Which?
- **`%` formatting**: older code, less flexible
- **`.format()`**: clearer placeholders, reordering
- **f-strings**: most concise, can embed expressions directly

### Challenge Yourself:
- Format a floating-point number: `f"Value: {pi:.2f}"`.
- Create a multi-line f-string for a mini report.
- Combine string methods and f-strings: `f"{name.upper()} is awesome!"`.

---

## 6. `06_escape.py` – Taming Special Characters

```python
# Escaping single quote
string1 = 'He said, \'Hello!\''

# Escaping double quote
string2 = "She replied, \"Hi!\""

# New line (\n) and tab (\t)
poem = "Roses are red,\nViolets are blue,\nPython is fun,\nAnd so are you!"
print(poem)
```

### Common Escape Sequences:
- **`\n`**: new line
- **`\t`**: tab
- **`\'`**, **`\"`**: literal quotes inside quotes
- **`\\`**: a single backslash `\`

### Play With Escapes:
- Write a path on Windows: `"C:\\Users\\You\\Documents"`.
- Create a small ASCII art box using `\n` and string concatenation.

---

## 🎓 Chapter 3 Wrap-Up: String Mastery!

You’ve explored how to:
1. **Create** strings in three different ways
2. **Index** and **slice** text (positive & negative)
3. **Apply** powerful built-in string methods
4. **Format** messages with `%`, `.format()`, and f-strings
5. **Escape** special characters for complex text

### Real-World Skills Unlocked:
- Building user-friendly command-line prompts
- Processing and cleaning text data
- Generating dynamic reports and messages
- Crafting simple text-based games or story engines

### What’s Next?
In **Chapter 4: Lists & Tuples**, you’ll learn how to group and organize multiple values, iterate over them, and perform list comprehensions to write concise, Pythonic code.

Keep practicing: Experiment with new methods you discover in the Python docs, and remember—strings are everywhere in real software, from web pages to data files. Mastering them now unlocks powerful possibilities later! 🚀
