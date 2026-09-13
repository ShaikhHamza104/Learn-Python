# 📚 Topic: Dictionaries and Sets Practice (Exercises)

Hands-on exercises exploring dictionary lookups with `.get()`, set deduplication with `.update()`, type hashing nuances (`18` vs. `"18"`, `20` vs. `20.0`), dictionary key uniqueness vs. value repetition, and set element hashability constraints.

## 📂 What's in this folder

| File | Description |
|---|---|
| `problem1.py` | Hindi-to-English translation dictionary using user input formatted with `.capitalize()` and queried safely using `.get()`. |
| `problem2.py` | Prompts for 8 numbers, loads them into a set using `.update()`, and prints the set to demonstrate automatic duplicate deduplication. |
| `problem3.py` | Confirms that a set can simultaneously hold both the integer `18` and string `"18"` because their types and hashes differ. |
| `problem4.py` | Demonstrates set deduplication with numeric equality: adding `20`, `20.0`, and `"20"` produces a set of length 2 because `20 == 20.0`. |
| `problem5.py` | Verifies that empty curly braces `s = {}` create a `<class 'dict'>`, confirming that `set()` must be used to create an empty set. |
| `problem6.py` | Gathers 4 friends' names and favorite programming languages using `input()` and builds a dictionary using `.update()`. |
| `problem7.py` | Demonstrates dictionary key uniqueness by reassigning an existing key (`"Harry"`), overwriting its prior value. |
| `problem8.py` | Demonstrates that while dictionary keys must be unique, different keys (`"Harry"` and `"Hamza"`) can share identical values. |
| `problem9.py` | Demonstrates unhashable type restrictions by attempting to store a mutable list `[1, 2]` inside a set, triggering a `TypeError`. |

## 💡 Key points

1. **Problem 1 (`problem1.py`)**: `dict.get(key)` provides safe lookups, returning `None` instead of throwing a `KeyError` if the key is missing.
2. **Problem 2 (`problem2.py`)**: Sets automatically eliminate duplicate entries when populated via `.update()`, storing only distinct items.
3. **Problem 3 (`problem3.py`)**: Type matters in sets: numeric `18` and string `"18"` are distinct objects with different types and hashes.
4. **Problem 4 (`problem4.py`)**: In Python numeric equality, `20 == 20.0` evaluates to `True` with identical hash values, causing sets to treat them as duplicate entries.
5. **Problem 5 (`problem5.py`)**: An empty literal `{}` constructs a dictionary; `set()` is required to initialize an empty set.
6. **Problem 6 (`problem6.py`)**: Dictionaries can be dynamically populated from user input using `.update({key: val})` or direct key assignment.
7. **Problem 7 (`problem7.py`)**: Assigning to an existing dictionary key overwrites the existing value in-place.
8. **Problem 8 (`problem8.py`)**: Dictionary keys must be unique and hashable, but multiple keys are permitted to reference identical values.
9. **Problem 9 (`problem9.py`)**: Set elements must be hashable and immutable; including a mutable list inside a set raises `TypeError: unhashable type: 'list'`.

## 🧠 Beginner tip

Remember that `20` and `20.0` are considered duplicate elements in a Python set because `20 == 20.0` and `hash(20) == hash(20.0)`. If you need to distinguish integers from floats with equal numerical values, track their types explicitly or convert them to strings.

## 📊 Where this is used in Data Science

Set operations provide high-speed deduplication across millions of records, while dictionaries form the basis for categorical mappings, encoding lookup tables, and configuration schemas. Understanding hashability and unhashable types is crucial when grouping by keys in Pandas or using custom objects as indices.

## 🏃 How to Run Each Exercise

Run each exercise script from your terminal:

```bash
python problem1.py
python problem2.py
python problem3.py
python problem4.py
python problem5.py
python problem6.py
python problem7.py
python problem8.py
python problem9.py
```
*(Note: `problem9.py` demonstrates an expected `TypeError` to illustrate set hashability rules).*

## 📖 Related Lessons

- [Chapter 05 - Dictionaries and Sets](../chapter_05_dicts_sets/README.md)

## ⏭️ What's Next

- [Chapter 06 - Control Flow](../chapter_06_control_flow/README.md)
