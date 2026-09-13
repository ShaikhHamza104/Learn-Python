# 📚 Topic: Iterators & Generators Practice (Exercises)

This folder contains 3 hands-on practice problems designed to reinforce the mechanics of Python iterators and generators. The exercises focus on implementing custom iterable classes adhering to the iterator protocol, creating on-demand generator functions using `yield`, and measuring memory efficiency with generator expressions.

---

## 📂 What's in this folder

| File | Description |
| --- | --- |
| `problem1.py` | Building a custom `Countdown` iterator class implementing `__iter__()`, `__next__()`, and `StopIteration` |
| `problem2.py` | Implementing a memory-efficient `fibonacci_gen()` generator function yielding numbers up to a limit |
| `problem3.py` | Profiling and comparing memory usage between generator expressions and list comprehensions using `sys.getsizeof()` |

---

## 💡 Key points

1. **Custom Iterator Implementation (`problem1.py`)**: Demonstrates the full iterator protocol by creating a class with `__iter__()` returning `self` and `__next__()` producing descending numbers until raising `StopIteration` when the counter reaches zero.
2. **Generating Sequences with `yield` (`problem2.py`)**: Implements an on-demand Fibonacci generator function that produces each subsequent number using `yield` without storing the growing sequence in memory.
3. **Memory Profiling of Lazy Evaluation (`problem3.py`)**: Compares memory consumption for 100,000 integers generated eagerly via a list comprehension against a lazy generator expression using `sys.getsizeof()`.

---

## 🧠 Beginner tip

When writing a generator function, never use `return <value>` to emit sequence items—always use `yield <value>`. In Python generator functions, calling `return <value>` halts the generator immediately and attaches the value to a `StopIteration` exception, which will terminate consumer loops prematurely.

---

## 📊 Where this is used in Data Science

- **Custom Epoch Shufflers**: Deep learning frameworks wrap dataset indices inside custom iterator classes (`__iter__`, `__next__`) to cleanly iterate through batches and shuffle sample indices across training epochs.
- **Generating Synthetic Training Series**: Time-series modeling and simulation scripts use generator functions to synthesize pseudo-random walk data or Fibonacci sequences on the fly without RAM consumption.
- **Resource Monitoring & Profiling**: Memory-profiling scripts verify memory consumption of feature transformations using `sys.getsizeof()` before deploying data-loading pipelines into constrained container environments.

---

## 🏃 How to Run Each Exercise

Execute each problem from the command line using Python:

```bash
# Problem 1: Custom Countdown iterator
python problem1.py

# Problem 2: Fibonacci generator function
python problem2.py

# Problem 3: Memory benchmark (list comprehension vs generator expression)
python problem3.py
```

---

## 📖 Related Lessons

Review the complete syntax and architectural details for iterators and generators in **[Chapter 17 — Iterators & Generators](../chapter_17_iterators_generators/README.md)**.

---

## ⏭️ What's Next

Explore iterator combinatorics and functional iteration tools in **[Chapter 18 — Itertools Module](../chapter_18_itertools/README.md)**!
