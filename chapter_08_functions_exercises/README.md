# 📚 Topic: Functions Practice (Exercises)

Hands-on exercises applying function declarations, return statements, mathematical formula implementations, output formatting with `print(..., end="")`, recursive summation and pattern generation, unit conversion helpers, list sanitization with `.strip()`, and loop encapsulation.

## 📂 What's in this folder

| File | Description |
|---|---|
| `problem1.py` | Defines a function `greatest(a, b, c)` returning the largest of 3 numbers using conditional branching. |
| `problem2.py` | Implements a temperature conversion function calculating Celsius from Fahrenheit using `5 * (f - 32) / 9` and `round()`. |
| `problem3.py` | Demonstrates inline printing without automatic newline termination using the `end=''` parameter in `print()`. |
| `problem4.py` | Calculates the sum of the first `n` natural numbers using a recursive function `sum(n)`. |
| `problem5.py` | Prints an inverted star pattern of `n` rows recursively using `pattern(n)` and base case `n == 0`. |
| `problem6.py` | Converts inches to centimeters (`i * 2.54`) and demonstrates keyword parameter calling (`itc(i=i)`). |
| `problem7.py` | Implements a function `rem(l, word)` to filter out matching words from a list and apply `.strip(word)` to remaining elements. |
| `problem8.py` | Encapsulates a multiplication table generation loop inside a reusable function `multiplication(num)`. |

## 💡 Key points

1. **Problem 1 (`problem1.py`)**: Demonstrates returning computed values from a function rather than printing them directly, allowing the caller to store or process the result.
2. **Problem 2 (`problem2.py`)**: Applies mathematical formulas within a function and rounds floating-point results with `round(val, 2)`.
3. **Problem 3 (`problem3.py`)**: Overrides Python's default newline behavior in `print()` by passing a custom `end=''` delimiter.
4. **Problem 4 (`problem4.py`)**: Implements recursive summation with a clear base case (`if n == 1: return 1`), reducing the problem step-by-step (`sum(n - 1) + n`).
5. **Problem 5 (`problem5.py`)**: Uses recursion for control flow and output generation, terminating when the row count reaches zero (`if n == 0: return`).
6. **Problem 6 (`problem6.py`)**: Illustrates conversion factors inside single-purpose helper functions invoked with explicit keyword arguments.
7. **Problem 7 (`problem7.py`)**: Combines conditional filtering (`if not (item == word)`) and string stripping (`item.strip(word)`) within a list transformation function.
8. **Problem 8 (`problem8.py`)**: Wraps repetitive loop logic into a parameterized, reusable function call.

## 🧠 Beginner tip

In recursive functions like `problem4.py` and `problem5.py`, always define the base case at the very top of the function! If your base case is missing or incorrect, Python will keep calling the function indefinitely until exceeding the maximum recursion depth (`RecursionError: maximum recursion depth exceeded`).

## 📊 Where this is used in Data Science

Encapsulating logic into modular functions is the cornerstone of clean data engineering. Functions define custom converters (e.g., Fahrenheit to Celsius or inches to cm), feature cleaning routines (`rem(l, word)`), and transformation pipelines that can be cleanly mapped over Pandas columns using `df['col'].apply(func)`.

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
```

## 📖 Related Lessons

- [Chapter 08 - Functions](../chapter_08_functions/README.md)

## ⏭️ What's Next

- [Chapter 09 - File Handling](../chapter_09_file_handling/README.md)
