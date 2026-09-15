# 📚 Topic: Regular Expressions Practice (Exercises)

This folder contains 5 hands-on practice problems designed to strengthen your mastery of regular expressions (`re` module) in Python. Regular expressions provide a specialized pattern-matching language used to search, validate, and clean textual data. Working through these exercises will build your muscle memory for extracting data, sanitizing sensitive strings, and enforcing strict input validation rules.

---

## 📂 What's in this folder

| File | What it teaches |
|------|------------------|
| `problem1.py` | Prompts the user for a sentence and extracts all email addresses matching an email regex pattern using `re.findall()`. |
| `problem2.py` | Validates whether a user-entered phone number is a valid 10-digit Indian phone number starting with digits 6–9 using `re.fullmatch()`. |
| `problem3.py` | Masks every digit in a user-provided sentence by replacing each number with a `#` symbol using `re.sub()`. |
| `problem4.py` | Finds and extracts all words starting with a capital letter in a user-provided sentence using word boundaries (`\b`) and `re.findall()`. |
| `problem5.py` | Audits password security by verifying length (8+ characters) and the presence of uppercase letters, digits, and special characters using `re.search()`. |

---

## 💡 Key points

1. **`problem1.py` practices structured extraction**: Uses character classes and repetition qualifiers (`[\w.+-]+@...`) with `re.findall()` to pull multiple structured patterns out of unstructured sentences.
2. **`problem2.py` practices strict boundary validation**: Anchors with `^` and `$` combined with `re.fullmatch()` ensure the entire input string satisfies the format rather than matching a partial substring.
3. **`problem3.py` practices text sanitization**: Uses `re.sub()` to substitute matched patterns, an essential technique for masking private or sensitive numbers.
4. **`problem4.py` practices word boundaries**: Employs `\b` word boundary anchors with `[A-Z]` to identify capitalized tokens without matching punctuation or middle characters.
5. **`problem5.py` practices composite rule checking**: Combines multiple independent `re.search()` evaluations to enforce password complexity without overly convoluted single-pattern regexes.

---

## 🧠 Beginner tip

When validating patterns (such as phone numbers or passwords), always test your script with both valid and invalid inputs! Try numbers that are too short, numbers with letters, or passwords missing a special character to ensure your validation correctly flags every edge case.

---

## 📊 Where this is used in Data Science

Text cleaning and regular expressions are indispensable for Natural Language Processing (NLP) and Exploratory Data Analysis (EDA). Before feeding text into sentiment models or language classifiers, data scientists use regex to strip HTML tags, remove URLs, standardize phone and email fields, and redact personally identifiable information (PII) from user-submitted survey feedback and customer logs.

---

## 🏃 How to Run Each Exercise

All problem files are interactive and accept user input from the console:

```bash
# Problem 1: Email Extractor
python problem1.py

# Problem 2: Phone Number Validator
python problem2.py

# Problem 3: Hide Digits in Text
python problem3.py

# Problem 4: Find Capitalized Words
python problem4.py

# Problem 5: Password Strength Checker
python problem5.py
```

---

## 📖 Related Lessons
Need a refresher on regular expression syntax? Review the lesson materials in **[Chapter 15 — Regular Expressions](../chapter_15_regex/README.md)**.

---

## ⏭️ What's Next?
Once you are confident with text processing, head to **[Chapter 16 — Collections Module](../chapter_16_collections/README.md)** to learn about specialized container types like `Counter`, `defaultdict`, and `deque`!
