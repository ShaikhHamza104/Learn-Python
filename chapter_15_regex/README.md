# 📚 Topic: Regular Expressions (re module)

Regular expressions (regex) provide a concise syntax for searching, extracting, and modifying text patterns. Python's built-in `re` module allows you to find substrings, extract structured components with capture groups, mask sensitive information, and validate data formats such as email addresses, phone numbers, and dates before processing.

---

## 📂 What's in this folder

| File | What it teaches |
| --- | --- |
| `01_intro_re.py` | Basic pattern matching using `re.match()`, `re.search()`, `re.findall()`, and `.group()` |
| `02_groups_and_substitution.py` | Numbered and named capturing groups, regex replacements with `re.sub()`, and custom splitting with `re.split()` |
| `03_common_patterns.py` | Production validation patterns for emails, phone numbers, and dates using `re.fullmatch()` |

---

## 💡 Key points

1. **Locating Matches (`01_intro_re.py`)**: `re.match()` checks for matches strictly at the start of a string, `re.search()` locates the first match anywhere in the string, and `re.findall()` returns all non-overlapping matches as a list of strings.
2. **Accessing Matched Substrings (`01_intro_re.py`)**: Calling `.group()` on a `Match` object returns the exact matched text segment rather than the metadata container.
3. **Numbered & Named Capturing Groups (`02_groups_and_substitution.py`)**: Enclosing sub-patterns in parentheses `(\d{2})` allows extracting sub-components via `match.group(1)`, `match.group(2)`, or named syntax `(?P<year>\d{4})` accessed via `match.group("year")`.
4. **Pattern Replacement & Group Backreferences (`02_groups_and_substitution.py`)**: `re.sub(pattern, replacement, string)` replaces matches across strings (such as masking digits with `*`), while backreferences (like `r"\3-\2-\1"`) rearrange captured components into new date formats.
5. **Pattern-Based String Splitting (`02_groups_and_substitution.py`)**: `re.split(r"[,;]\s*", string)` breaks strings on complex delimiters (commas, semicolons, and arbitrary trailing whitespace) in a single operation.
6. **Strict Entire-String Validation (`03_common_patterns.py`)**: `re.fullmatch(pattern, text)` requires the pattern to match from start `^` to end `$`, making it the correct method for validating input forms like 10-digit phone numbers (`^[6-9]\d{9}$`) and email addresses.

---

## 🧠 Beginner tip

Always use raw strings (prefixed with `r"..."`, like `r"\d+"`) for regular expression patterns in Python. Without the `r` prefix, Python's string parser interprets backslashes as string escape sequences (e.g., `\b` for backspace, `\n` for newline) before regex ever receives the pattern, resulting in invalid regular expressions or subtle matching bugs.

---

## 📊 Where this is used in Data Science

- **Text Preprocessing & NLP Pipelines**: Before feeding text into tokenizers or vectorizers, NLP workflows use regex to strip HTML tags, remove URLs, standardize punctuation, and isolate emoji characters.
- **Log Parsing & Metric Extraction**: Data engineers parse unstructured server and cluster logs using named regex groups `(?P<timestamp>...) (?P<status_code>\d{3})` to extract structured data into Pandas DataFrames.
- **Data Cleaning & Deduplication**: Real-world customer records often have inconsistent phone formats (`+91-9876543210`, `(987) 654-3210`, `9876543210`). Regex standardizes phone numbers and cleans dirty postal codes across millions of records.

---

## 🛠️ Code Examples

### Finding and Extracting Matches
```python
import re

text = "Invoice #4092 created on 2026-05-12. Total: $450."

# Extract all numeric sequences
numbers = re.findall(r"\d+", text)
print("Extracted numbers:", numbers)  # ['4092', '2026', '05', '12', '450']

# Extract date with capturing groups
date_match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
if date_match:
    year, month, day = date_match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")
```

### Validating Inputs with `re.fullmatch`
```python
import re

def is_valid_username(name):
    # 3 to 16 alphanumeric characters or underscores
    pattern = r"^[a-zA-Z0-9_]{3,16}$"
    return bool(re.fullmatch(pattern, name))

print(is_valid_username("hamza_104"))  # True
print(is_valid_username("bad user!"))  # False
```

### Reformatting Strings with Backreferences
```python
import re

# Convert 'YYYY-MM-DD' to 'DD/MM/YYYY'
raw_date = "2026-09-13"
formatted = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", raw_date)
print("Formatted date:", formatted)  # 13/09/2026
```

---

## 🏋️ Practice Exercises

Test your pattern matching and data validation skills across 5 targeted challenges in **[chapter_15_regex_exercises/](../chapter_15_regex_exercises/README.md)**!

---

## ⏭️ What's Next

Explore specialized high-performance container data types like `namedtuple`, `deque`, and `Counter` in **[Chapter 16 — Collections Module](../chapter_16_collections/README.md)**!
