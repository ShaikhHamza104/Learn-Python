# 🐍 Chapter 18 — Itertools Module: High-Performance Iterator Building Blocks 🔁

Welcome to Chapter 18! Python's standard library provides the `itertools` module, a collection of fast, memory-efficient tools for creating complex iterators inspired by constructs from APL, Haskell, and SML. In this chapter, you will master all **16 itertools functions**, categorized into infinite, terminating, and combinatoric iterators.

---

## 📂 Files in This Chapter

| # | File | Category | Quick Peek |
|---|---|---|---|
| 01 | `01_accumulate.py` | Terminating | Running totals & accumulated results (`accumulate([1, 2, 3])` -> `1, 3, 6`) |
| 02 | `02_chain.py` | Terminating | Chaining multiple iterables consecutively (`chain(li1, li2)`) |
| 03 | `03_compress.py` | Terminating | Filtering elements using a boolean mask (`compress(data, selectors)`) |
| 04 | `04_count.py` | Infinite | Infinite arithmetic progression (`count(start=10, step=2)`) |
| 05 | `05_cycle.py` | Infinite | Cycling indefinitely through an iterable (`cycle(["A", "B", "C"])`) |
| 06 | `06_dropwhile.py` | Terminating | Dropping elements while predicate holds `True`, then yields rest |
| 07 | `07_filterfalse.py` | Terminating | Yielding elements where predicate returns `False` |
| 08 | `08_groupby.py` | Terminating | Grouping consecutive matching keys from sorted data |
| 09 | `09_islice.py` | Terminating | Slicing iterators by index without loading into a list |
| 10 | `10_permutations.py` | Combinatoric | All possible ordered arrangements of elements |
| 11 | `11_product.py` | Combinatoric | Cartesian product (equivalent to nested `for` loops) |
| 12 | `12_repeat.py` | Infinite/Count | Yielding an object repeatedly (`repeat(val, times)`) |
| 13 | `13_starmap.py` | Terminating | Mapping functions over pre-zipped argument tuples |
| 14 | `14_takewhile.py` | Terminating | Taking elements while predicate is `True`, stops immediately at `False` |
| 15 | `15_tee.py` | Terminating | Splitting one iterator into $n$ independent iterators |
| 16 | `16_zip_longest.py` | Terminating | Zipping iterables of unequal length using a `fillvalue` |

---

## ♾️ 1. Infinite Iterators (`count`, `cycle`, `repeat`)

These iterators generate endless streams. Use them with `break` or `islice` to prevent infinite loops:

```python
from itertools import count, cycle, repeat, islice

# count(start, step): 10, 12, 14, ...
for n in islice(count(10, 2), 4):
    print(n)  # 10, 12, 14, 16

# cycle(iterable): A, B, A, B, A, B, ...
colors = cycle(["Red", "Green"])
print(next(colors))  # Red
print(next(colors))  # Green
print(next(colors))  # Red

# repeat(elem, n): repeats an object n times
print(list(repeat("Python", 3)))  # ['Python', 'Python', 'Python']
```

---

## ✂️ 2. Terminating & Slicing Iterators

```python
from itertools import accumulate, chain, compress, dropwhile, takewhile, islice, zip_longest

# accumulate: running total
print(list(accumulate([1, 2, 3, 4])))  # [1, 3, 6, 10]

# chain: flatten multiple lists
print(list(chain([1, 2], [3, 4], [5])))  # [1, 2, 3, 4, 5]

# compress: filter by boolean selector
data = ["A", "B", "C", "D"]
mask = [True, False, True, False]
print(list(compress(data, mask)))  # ['A', 'C']

# takewhile vs dropwhile
nums = [1, 3, 5, 8, 2, 4]
print(list(takewhile(lambda x: x < 5, nums)))  # [1, 3] (stops at 5)
print(list(dropwhile(lambda x: x < 5, nums)))  # [5, 8, 2, 4] (starts at 5)

# zip_longest: padding unequal lengths
print(list(zip_longest([1, 2], ["a", "b", "c"], fillvalue="-")))
# [(1, 'a'), (2, 'b'), ('-', 'c')]
```

---

## 🎲 3. Combinatorics (`permutations`, `product`)

```python
from itertools import permutations, product

# Cartesian product (Cartesian grid: suits x ranks)
suits = ["♠", "♥"]
ranks = ["A", "K"]
deck = list(product(suits, ranks))
print(deck)  # [('♠', 'A'), ('♠', 'K'), ('♥', 'A'), ('♥', 'K')]

# Permutations (order matters)
print(list(permutations(["A", "B", "C"], 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

---

## 👥 4. Grouping Data with `groupby`

> [!WARNING]
> `groupby()` only groups **consecutive** matching items. You must sort your input iterable by the grouping key first!

```python
from itertools import groupby

people = [
    {"role": "dev", "name": "Hamza"},
    {"role": "dev", "name": "Ali"},
    {"role": "design", "name": "Sara"}
]

# Sort by key first!
people.sort(key=lambda p: p["role"])

for role, group in groupby(people, key=lambda p: p["role"]):
    names = [p["name"] for p in group]
    print(f"{role}: {', '.join(names)}")
# design: Sara
# dev: Hamza, Ali
```

---

## ⏭️ What's Next?
Next, explore decorators, caching, and function transformations in **[Chapter 19 — Functional Tools](../chapter_19_functional_tools/README.md)**!
