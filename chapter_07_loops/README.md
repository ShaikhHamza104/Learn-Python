# 📚 Topic: Loops

Loops allow Python programs to execute blocks of code repeatedly without duplicate statements. This chapter covers counter-driven `while` loops, index-based list traversal, `for` loops across diverse iterable types (strings, lists, tuples), numeric sequencing with `range(start, stop, step)`, loop completion handling, flow interruption with `break` and `continue`, and placeholder definitions using `pass`.

## 📂 What's in this folder

| File | What it teaches |
|---|---|
| `01_loop.py` | Contrasts repetitive manual `print()` statements against automated iteration with `for i in range(1, 6)`. |
| `02_while_loop.py` | Basic `while` loop syntax driven by a manual counter variable (`i = 1`, `while i < 6`, `i += 1`). |
| `03_list_using_while.py` | Iterating through a list of names using a `while` loop bound by `len(l)` and an index counter. |
| `04_for_loop.py` | Direct element iteration using `for` loops across strings, lists, and tuples without index tracking. |
| `05_range.py` | Generating numeric sequences using `range(stop)` and `range(start, stop, step)` for step increments. |
| `06_for_with_else.py` | Executing logic after a `for` loop completes its iteration sequence. |
| `07_break_and_continue.py` | Altering loop flow: immediately terminating iterations with `break` and skipping specific iterations with `continue`. |
| `08_pass.py` | Using the `pass` null-operation statement as a syntactic placeholder in loops, contrasted with a `while` counter loop. |

## 💡 Key points

1. **For vs. While Loops**: Use `for` loops when iterating over known collections or bounded sequences; use `while` loops when repetition is governed by an ongoing state or condition.
2. **Infinite Loop Prevention**: Always ensure the condition of a `while` loop eventually becomes `False` (such as incrementing counter `i += 1`).
3. **Range Step Parameter**: `range(start, stop, step)` generates numbers up to but excluding `stop`, advancing by `step` increments (e.g., `range(1, 10, 2)` produces odd numbers).
4. **Break vs. Continue**: `break` halts the entire loop immediately; `continue` halts only the current cycle and skips ahead to the next iteration.
5. **The `pass` Statement**: `pass` is a syntactic placeholder that performs no operation, preventing syntax errors in unfilled code blocks.

## 🧠 Beginner tip

In `while` loops, never forget to update your loop counter (e.g., `i += 1`) inside the loop body! If you omit the update step, `i` will stay unchanged, the loop condition will remain permanently `True`, and your program will hang in an infinite loop.

## 📊 Where this is used in Data Science

Iteration powers batch dataset processing, training loops in machine learning (epochs and mini-batches), grid searches over hyperparameter combinations, simulations, and sequential data transformation when vectorization is not feasible.

## 🛠️ Code Examples

### While Loop Counter (`02_while_loop.py`)
```python
i = 1
while i < 6:
    print(i)
    i += 1
```

### Direct Iteration over Iterables (`04_for_loop.py`)
```python
for char in "Hamza":
    print(char)

for item in ["Harry", "Rohan", "Rahul"]:
    print(item)
```

### Range with Step (`05_range.py`)
```python
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9
```

### Flow Control with Break & Continue (`07_break_and_continue.py`)
```python
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop loop at 7
    print(i)
```

## 🏋️ Practice Exercises

Sharpen your loop control skills with the exercises in the practice folder:
- [Chapter 07 Exercises](../chapter_07_loops_exercises/README.md)

## ⏭️ What's Next

- [Chapter 08 - Functions](../chapter_08_functions/README.md)
