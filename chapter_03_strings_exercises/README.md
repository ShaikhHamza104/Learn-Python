# 📚 Topic: Strings Practice (Exercises)

Hands-on exercises for mastering string manipulation in Python, including storing user-entered strings in lists, template placeholder replacement with chained `.replace()`, detecting substrings with `.find()`, sanitizing whitespace, and using escape characters like `\t`.

## 📂 What's in this folder

| File | Description |
|---|---|
| `problem1.py` | Prompts for 7 fruit names sequentially with `input()`, stores each in a list using `.append()`, and prints the list. |
| `problem2.py` | Uses chained `.replace()` calls to substitute `<|Name|>` and `<|Date|>` placeholders in a multi-line letter template. |
| `problem3.py` | Detects double spaces (`"  "`) in a string using the `.find()` method inside a conditional statement. |
| `problem4.py` | Cleans irregular spacing by replacing double spaces (`"  "`) with single spaces (`" "`) using `.replace()`. |
| `problem5.py` | Demonstrates string formatting and tab alignment using the horizontal tab escape sequence `\t`. |

## 💡 Key points

1. **Problem 1 (`problem1.py`)**: `input()` gathers text input as strings, which can be stored dynamically into collections like lists using `.append()`.
2. **Problem 2 (`problem2.py`)**: Demonstrates method chaining with `.replace()`, substituting multiple template placeholders sequentially without mutating the original string.
3. **Problem 3 (`problem3.py`)**: `.find()` searches for substring occurrences and returns the start index (or `-1` if not found).
4. **Problem 4 (`problem4.py`)**: Uses `.replace("  ", " ")` for basic whitespace sanitization, creating a cleaned string copy.
5. **Problem 5 (`problem5.py`)**: Utilizes escape sequences such as `\t` (horizontal tab) to structure and space inline text.

## 🧠 Beginner tip

Be cautious when using `.find()` inside an `if` condition like `if string.find("  "):`! If the match is found at the very beginning of the string (index `0`), Python treats `0` as falsy, causing the `if` block not to execute. The safer, canonical pattern is `if string.find("  ") != -1:` or simply using the membership operator `if "  " in string:`.

## 📊 Where this is used in Data Science

String sanitization is a mandatory early stage of data prep. Unstructured text datasets (surveys, scraped webpages, customer reviews) frequently contain irregular whitespace, placeholder tokens, and escape characters. Techniques like replacing double spaces, filling templates, and verifying substring occurrences are foundational to text cleaning pipelines before NLP tokenization.

## 🏃 How to Run Each Exercise

Run each exercise script from your terminal:

```bash
python problem1.py
python problem2.py
python problem3.py
python problem4.py
python problem5.py
```

## 📖 Related Lessons

- [Chapter 03 - Strings](../chapter_03_strings/README.md)

## ⏭️ What's Next

- [Chapter 04 - Lists and Tuples](../chapter_04_lists_tuples/README.md)
