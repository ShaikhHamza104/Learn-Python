# 📚 Topic: Control Flow Practice (Exercises)

Hands-on exercises applying conditional logic: comparing multiple numbers with compound `and` vs. `max()`, evaluating composite passing thresholds, spam keyword filtering using `or`, string length boundary validation, collection membership lookup with `in`, tiered grading scales with input validation, and case-insensitive substring searching.

## 📂 What's in this folder

| File | Description |
|---|---|
| `problem1.py` | Finds the greatest of 4 numbers using two approaches: compound boolean comparisons in an `if-elif` ladder and a list with `max()`. |
| `problem2.py` | Evaluates student exam results requiring both >= 40% overall and >= 33 marks in each of 3 individual subjects. |
| `problem3.py` | Detects spam comments by checking whether any of 4 flagged phrases occur in user text using chained `or` membership tests. |
| `problem4.py` | Checks username string length and alerts if the input contains fewer than 10 characters using `len()`. |
| `problem5.py` | Checks whether a user's capitalized name exists within a predefined list of names using the `in` operator. |
| `problem6.py` | Assigns letter grades (`Ex`, `A`, `B`, `C`, `D`, `F`) from score inputs with an initial boundary check (`0` to `100`). |
| `problem7.py` | Performs a case-insensitive keyword search to check if a specific name is mentioned in user post text using `.lower()`. |

## 💡 Key points

1. **Problem 1 (`problem1.py`)**: Comparing multiple variables directly with `and` works for small fixed sets, but storing values in a list and using built-in `max()` is cleaner and scales to any number of items.
2. **Problem 2 (`problem2.py`)**: Compound conditions using `and` require every sub-condition to evaluate to `True` for the overall expression to pass.
3. **Problem 3 (`problem3.py`)**: Substring detection with `in` combined with logical `or` allows matching against a list of blocked keywords or spam phrases.
4. **Problem 4 (`problem4.py`)**: Validates input boundaries by checking string character counts with `len()`.
5. **Problem 5 (`problem5.py`)**: Uses the `in` membership operator to perform fast lookups against lists of allowed values.
6. **Problem 6 (`problem6.py`)**: Validates input bounds (`< 0 or > 100`) before cascading through descending threshold checks (`>= 90`, `>= 80`, etc.).
7. **Problem 7 (`problem7.py`)**: Normalizes text casing using `.lower()` on both target and corpus before substring matching to guarantee case insensitivity.

## 🧠 Beginner tip

When checking string membership, casing matters! `"Harry" in "harry is coding"` evaluates to `False`. To avoid missing matches due to capitalization differences, normalize both strings to lowercase first: `target.lower() in text.lower()`.

## 📊 Where this is used in Data Science

Conditional evaluation powers rule-based classification, spam filtering, data sanitization, and outlier detection. Text filtering via keyword matching (`p in text`) is used in content moderation and sentiment analysis pipelines, while compound range checks (`mark < 0 or mark > 100`) are essential for data validation and schema integrity enforcement.

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
```

## 📖 Related Lessons

- [Chapter 06 - Control Flow](../chapter_06_control_flow/README.md)

## ⏭️ What's Next

- [Chapter 07 - Loops](../chapter_07_loops/README.md)
