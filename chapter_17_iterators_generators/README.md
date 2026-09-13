# 🐍 Chapter 17 — Iterators & Generators: Memory-Efficient Iteration ⚙️

Welcome to Chapter 17! In Python, loops don't just work by magic — they rely on the **Iterator Protocol**. In this chapter, you will look under the hood of Python's `for` loops, build your own custom iterators, master **Generator Functions** with `yield`, write **Generator Expressions**, and see firsthand how generators allow you to process massive or infinite data streams using virtually zero memory!

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_iterator_protocol.py` | The Iterator Protocol | `iter()`, `next()`, `StopIteration`, custom `MeraRange` class |
| 02 | `02_generator_functions.py` | Generator Functions & `yield` | State preservation, infinite series, generator pipelines |
| 03 | `03_generator_expressions.py` | Generator Expressions | `(x**2 for x in data)` vs `[x**2 for x in data]`, memory comparison |

---

## ⚙️ 1. The Iterator Protocol (`01_iterator_protocol.py`)

An **Iterable** is any object you can loop over (it defines `__iter__()`).
An **Iterator** is the object that actually traverses the values one by one (it defines both `__iter__()` and `__next__()`).

```python
numbers = [10, 20, 30]

# What Python's for loop does behind the scenes:
iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
# print(next(iterator))  # Raises StopIteration when items are exhausted!
```

### Custom Iterator Class:
```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for n in CountDown(3):
    print(n)  # 3, 2, 1
```

---

## ⚡ 2. Generator Functions & `yield` (`02_generator_functions.py`)

Writing a custom iterator class with `__iter__` and `__next__` is verbose. **Generators** give you the exact same iterator protocol for free using functions and the `yield` keyword!

```python
def count_down_gen(start):
    while start > 0:
        yield start
        start -= 1

for num in count_down_gen(3):
    print(num)  # 3, 2, 1
```

### Key Superpowers of Generators:
1. **State Preservation**: Each `yield` pauses execution and remembers all local variables until the caller requests the next item.
2. **Infinite Streams**: A generator can generate data endlessly without crashing your computer's RAM:
   ```python
   def infinite_evens():
       n = 0
       while True:
           yield n
           n += 2
   ```
3. **Pipeline Chaining**: Generators can feed into other generators in an ETL data pipeline.

---

## 📈 3. Generator Expressions & Memory Savings (`03_generator_expressions.py`)

Generator expressions look identical to list comprehensions, except they use parentheses `()` instead of brackets `[]`:

```python
import sys

# List comprehension: calculates ALL items immediately and loads into RAM
full_list = [x for x in range(1000000)]

# Generator expression: calculates items ON THE FLY as requested
gen_expr = (x for x in range(1000000))

print("Memory of List (bytes):", sys.getsizeof(full_list))  # ~8.4 MB
print("Memory of Gen (bytes):", sys.getsizeof(gen_expr))   # ~200 Bytes!
```

---

## 🏋️ Practice Exercises
Put your iterator and generator skills to work with challenge tasks in **[chapter_17_exercises/](../chapter_17_exercises/README.md)**!

---

## ⏭️ What's Next?
Next, discover the ultimate toolkit of iterator building blocks in **[Chapter 18 — Itertools Module](../chapter_18_itertools/README.md)**!
