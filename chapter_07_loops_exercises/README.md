# 📚 Topic: Loops Practice (Exercises)

Hands-on exercises applying `for` and `while` loops, multiplication tables (forward and reverse), conditional string prefix filtering, prime number detection using `for...else`, arithmetic series summation, factorials, and 2D geometric star patterns (pyramids, triangles, and hollow squares).

## 📂 What's in this folder

| File | Description |
|---|---|
| `problem1.py` | Prints a multiplication table for a user-input number from 1 to 10 using a `for` loop and `range()`. |
| `problem2.py` | Iterates over a list of names and greets only those whose names start with `"S"` using `.startswith()`. |
| `problem3.py` | Generates a multiplication table from 1 to 10 using a counter-driven `while` loop instead of a `for` loop. |
| `problem4.py` | Determines whether an input integer is prime by searching for factors with a `for` loop and a `for...else` block. |
| `problem5.py` | Calculates the sum of the first `n` natural numbers using an accumulator in a `while` loop. |
| `problem6.py` | Computes the factorial of a user-entered number using a multiplicative accumulator in a `for` loop. |
| `problem7.py` | Generates a centered symmetric pyramid star pattern for `n` rows using leading spaces and odd star counts (`2*i - 1`). |
| `problem8.py` | Prints a right-angled triangle star pattern of height `n = 3` using nested `for` loops. |
| `problem9.py` | Prints a hollow square star pattern where boundary rows are filled and middle rows contain interior spaces. |
| `problem10.py` | Prints a multiplication table in reverse order (from 10 down to 1) using `range(10, 0, -1)`. |

## 💡 Key points

1. **Problem 1 (`problem1.py`)**: `range(1, 11)` produces a sequence from 1 to 10, ideal for generating multiplication tables with f-string formatting.
2. **Problem 2 (`problem2.py`)**: Demonstrates filtering list items inside an iteration using conditional prefix checks (`name.startswith("S")`).
3. **Problem 3 (`problem3.py`)**: Implements the same multiplication table logic using manual counter initialization (`i = 1`) and step increments (`i += 1`) inside a `while` loop.
4. **Problem 4 (`problem4.py`)**: The `for...else` construct executes the `else` block only when the loop completes without encountering a `break`, providing a clean syntax for prime verification.
5. **Problem 5 (`problem5.py`)**: Demonstrates accumulator summation (`total += i`) inside a `while` loop for series calculation.
6. **Problem 6 (`problem6.py`)**: Computes products across sequences (`fact *= i`), showing how initialization (`fact = 1`) differs from additive accumulators.
7. **Problem 7 (`problem7.py`)**: Combines string repetition (`" " * (n - i)` and `"*" * (2 * i - 1)`) to build centered 2D geometric patterns.
8. **Problem 8 (`problem8.py`)**: Demonstrates nested loop coordination where the inner loop's range is dynamically bound to the outer loop's index `i`.
9. **Problem 9 (`problem9.py`)**: Uses branch conditionals (`if i == 1 or i == n`) to distinguish filled borders from hollow interior rows.
10. **Problem 10 (`problem10.py`)**: Uses negative step arguments in `range(10, 0, -1)` to decrement indices and generate reverse sequences.

## 🧠 Beginner tip

The `else` block on a Python loop is unique! It runs **only if the loop finishes normally without hitting a `break`**. In prime checking (`problem4.py`), if any divisor divides `n`, the code triggers `break` and bypasses the `else` block; if no divisors are found, the `else` block runs and announces the number is prime.

## 📊 Where this is used in Data Science

Iterative algorithms underpin mathematical modeling, numerical optimization, and feature engineering. Accumulators and loops are used in convergence algorithms (e.g., gradient descent step loops), factorial calculations appear in probability distributions and combinatorics, and negative step ranges help in reverse time-series indexing.

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
python problem10.py
```

## 📖 Related Lessons

- [Chapter 07 - Loops](../chapter_07_loops/README.md)

## ⏭️ What's Next

- [Chapter 08 - Functions](../chapter_08_functions/README.md)
