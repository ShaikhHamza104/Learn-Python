# 📚 Topic: Iterators & Generators

Iteration is at the heart of Python programming. Behind every `for` loop lies the **Iterator Protocol**, powered by the built-in `iter()` and `next()` functions. Python makes creating custom iterators clean and memory-efficient through **generator functions** (using `yield`) and **generator expressions**, enabling you to process massive or infinite data streams on the fly without exhausting computer memory.

---

## 📂 What's in this folder

| File | What it teaches |
| --- | --- |
| `01_iterator_protocol.py` | The Iterator Protocol (`iter()`, `next()`, `StopIteration`), custom iterator classes (`MeraRange`), and loop mechanics |
| `02_generator_functions.py` | Implementing generators using `yield`, representing infinite streams, and chaining generator pipelines |
| `03_generator_expressions.py` | Lazy generator expressions `(x for x in data)` vs eager list comprehensions, and measuring memory with `sys.getsizeof` |

---

## 💡 Key points

1. **Iterables vs. Iterators (`01_iterator_protocol.py`)**: An iterable is any container you can loop over (implements `__iter__()`). Calling `iter(iterable)` returns an iterator object, which implements both `__iter__()` and `__next__()` to fetch items sequentially.
2. **The Mechanics of `for` Loops (`01_iterator_protocol.py`)**: Python's `for` loop works by requesting an iterator via `iter()`, repeatedly calling `next()`, and catching `StopIteration` to gracefully exit the loop when items are exhausted.
3. **Custom Iterator Protocol (`01_iterator_protocol.py`)**: Building a custom iterable class like `MeraRange` requires returning an iterator whose `__next__()` method maintains progression state and raises `StopIteration` upon reaching termination boundaries.
4. **Generator Functions with `yield` (`02_generator_functions.py`)**: A generator function uses `yield` instead of `return`. Each `yield` pauses execution and saves local function state, resuming immediately upon the next `next()` call.
5. **Infinite Data Streams & Pipeline Chaining (`02_generator_functions.py`)**: Generators can represent infinite sequences (such as `all_even()` with `while True: yield n`) and can be chained together (e.g. `sum(square_each(fibonacci_numbers(10)))`) so data flows item-by-item without full intermediate arrays.
6. **Generator Exhaustion (`02_generator_functions.py`)**: Once a generator yields its final value, it is exhausted and cannot be restarted; creating a fresh generator object requires calling the generator function again.
7. **Lazy Generator Expressions (`03_generator_expressions.py`)**: Replacing list comprehension brackets `[...]` with parentheses `(...)` creates a generator expression that computes items lazily on demand, dropping memory consumption from megabytes down to a few hundred bytes regardless of sequence length.

---

## 🧠 Beginner tip

Use list comprehensions `[x for x in data]` when you need to index, slice, sort, or iterate over the data multiple times. Use generator expressions `(x for x in data)` when you only need to stream through the data once (such as passing directly into `sum()`, `max()`, `any()`, or a single `for` loop). This simple habit prevents high memory usage when processing large datasets.

---

## 📊 Where this is used in Data Science

- **Streaming Multi-Gigabyte Datasets**: Processing 50 GB log files or genomic sequences line-by-line using generator expressions prevents out-of-memory (OOM) crashes by streaming single records into memory.
- **Deep Learning Batch Generators (PyTorch / TensorFlow)**: Dataset loaders rely on Python generators to fetch, augment, and yield one mini-batch of images or tensors to GPU memory per training step.
- **ETL Data Streaming Pipelines**: Multi-stage data transformation pipelines (cleaning -> tokenizing -> scoring) chain generators together so records stream seamlessly through transformations without saving huge intermediate CSVs or lists.

---

## 🛠️ Code Examples

### Manual Iterator Traversal
```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
# next(iterator) -> raises StopIteration
```

### Generator Function for Streaming
```python
def count_up(start, step=1):
    current = start
    while True:
        yield current
        current += step

stream = count_up(100, step=10)
print(next(stream))  # 100
print(next(stream))  # 110
```

### Generator Expression Passed into Aggregations
```python
import sys

# Lazy generator expression calculates on the fly
squares_gen = (x**2 for x in range(1_000_000))
print("Memory consumed:", sys.getsizeof(squares_gen), "bytes")  # ~200 bytes

# Consumed directly without intermediate list
total = sum(x**2 for x in range(1, 101))
print("Sum of squares:", total)
```

---

## 🏋️ Practice Exercises

Hone your skills building custom iterators and memory-efficient streaming generators in **[chapter_17_iterators_generators_exercises/](../chapter_17_iterators_generators_exercises/README.md)**!

---

## ⏭️ What's Next

Discover advanced combinatorial iterators and looping tools in **[Chapter 18 — Itertools Module](../chapter_18_itertools/README.md)**!
