# 📚 Topic: Lists and Tuples Practice (Exercises)

Practice exercises covering list creation and appending with user input, in-place sorting of numeric data, verifying tuple immutability, summing collections with `sum()`, and frequency counting with `.count()`.

## 📂 What's in this folder

| File | Description |
|---|---|
| `problem1.py` | Prompts for 7 fruit names from the user, stores them sequentially in a list using `.append()`, and displays the final list. |
| `problem2.py` | Collects marks for 6 students via `int(input())`, stores them in a list, sorts them in ascending order with `.sort()`, and prints the result. |
| `problem3.py` | Demonstrates tuple immutability with `t = (1, 2, 3, True, None)`, explaining why item reassignment (`t[0] = 90`) raises a `TypeError`. |
| `problem4.py` | Computes the total sum of a 4-element numeric list `[22, 27, 98, 89]` using Python's built-in `sum()` function. |
| `problem5.py` | Counts the occurrences of the number zero in the tuple `(7, 0, 8, 0, 0, 9)` using the `.count(0)` method. |

## 💡 Key points

1. **Problem 1 (`problem1.py`)**: Demonstrates dynamic list growth by appending user-entered string items one at a time using `.append()`.
2. **Problem 2 (`problem2.py`)**: Applies `.sort()` to arrange numeric student scores in-place from lowest to highest.
3. **Problem 3 (`problem3.py`)**: Validates that tuples are immutable data structures that cannot be modified after assignment.
4. **Problem 4 (`problem4.py`)**: Uses `sum()` to quickly aggregate all numerical items in an iterable without requiring manual loop accumulation.
5. **Problem 5 (`problem5.py`)**: Leverages `tuple.count(val)` to calculate frequency of a specific value without modifying the underlying sequence.

## 🧠 Beginner tip

Remember that `list.sort()` sorts the list in-place and returns `None`! Writing `mark_of_student = mark_of_student.sort()` will overwrite your list variable with `None`. Always call `mark_of_student.sort()` as a standalone statement.

## 📊 Where this is used in Data Science

Sorting values and calculating totals are standard operations in exploratory data analysis and feature engineering. In data preprocessing, counting zero values (`.count(0)`) or missing flags across tuples helps detect sparse data, while aggregating columns with `sum()` powers summary metrics in Pandas and NumPy.

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

- [Chapter 04 - Lists and Tuples](../chapter_04_lists_tuples/README.md)

## ⏭️ What's Next

- [Chapter 05 - Dictionaries and Sets](../chapter_05_dicts_sets/README.md)
