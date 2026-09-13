# 📚 Topic: Itertools Module

The Python standard library's `itertools` module provides a suite of fast, memory-efficient building blocks for iterator algebra. Inspired by functional languages like APL, Haskell, and SML, `itertools` functions return lazy iterators that calculate elements on demand. This chapter covers all 16 core itertools functions across infinite streams, terminating filters, data grouping, and combinatorial generation.

---

## 📂 What's in this folder

| File | What it teaches |
| --- | --- |
| `01_accumulate.py` | Cumulative sums and custom running accumulations (such as running products) |
| `02_chain.py` | Linking multiple iterables sequentially and flattening lists with `chain.from_iterable()` |
| `03_compress.py` | Filtering an iterable using boolean indicators from a selector mask |
| `04_count.py` | Creating infinite arithmetic progressions with configurable `start` and `step` values |
| `05_cycle.py` | Cycling indefinitely through an iterable sequence in a continuous loop |
| `06_dropwhile.py` | Dropping elements while a condition remains `True`, then yielding the remainder |
| `07_filterfalse.py` | Filtering elements where a predicate function returns `False` (complement of `filter()`) |
| `08_groupby.py` | Grouping consecutive items from pre-sorted iterables by a key function |
| `09_islice.py` | Slicing iterators by start, stop, and step indices without creating intermediate lists |
| `10_permutations.py` | Generating all possible ordered arrangements of elements for a specified length |
| `11_product.py` | Computing Cartesian products across multiple iterables and repeated sets |
| `12_repeat.py` | Emitting an object repeatedly for a specified count or indefinitely |
| `13_starmap.py` | Evaluating a function over argument tuples unpacked from an iterable |
| `14_takewhile.py` | Yielding elements while a predicate is `True` and halting at the first `False` |
| `15_tee.py` | Duplicating a single iterator into multiple independent iterators |
| `16_zip_longest.py` | Zipping sequences of unequal lengths with a fallback `fillvalue` |

---

## 💡 Key points

1. **Running Accumulations (`01_accumulate.py`)**: `accumulate(iterable, [func])` yields intermediate totals (defaulting to addition), producing cumulative sums or custom running products when passed a binary lambda like `lambda x, y: x * y`.
2. **Sequential Iteration & Flattening (`02_chain.py`)**: `chain(it1, it2, ...)` iterates across sequences end-to-end without concatenation, and `chain.from_iterable(nested)` flattens one level of nested collections lazily.
3. **Boolean Filtering (`03_compress.py`)**: `compress(data, selectors)` filters elements based on matching truthy values in the parallel `selectors` iterable, acting as a lightweight data mask.
4. **Infinite Counting & Cycling (`04_count.py`, `05_cycle.py`)**: `count(start, step)` produces unending numeric progressions, while `cycle(iterable)` loops over an iterable infinitely; both are paired with `islice()` to inspect bounded slices safely.
5. **Conditional Stream Truncation (`06_dropwhile.py`, `07_filterfalse.py`, `14_takewhile.py`)**: `takewhile()` stops yielding at the very first element where the predicate is false; `dropwhile()` discards until the predicate is false and yields all remaining elements; `filterfalse()` filters the entire sequence retaining items where the predicate returns false.
6. **Key Grouping Mechanics (`08_groupby.py`)**: `groupby(data, key=...)` bunches consecutive items sharing a key. **Critical**: inputs must be sorted by the key beforehand, as `groupby` generates a new group whenever the key changes.
7. **Zero-Copy Slicing (`09_islice.py`)**: `islice(iterable, start, stop, step)` slices streams by index without materializing items into a memory list, making it safe for infinite or huge generators.
8. **Combinatorial Generation (`10_permutations.py`, `11_product.py`)**: `permutations(p, r)` generates all order-dependent tuples of length $r$, while `product(*iterables, repeat=1)` computes Cartesian products equivalent to nested `for` loops.
9. **Argument Mapping & Duplication (`12_repeat.py`, `13_starmap.py`, `15_tee.py`, `16_zip_longest.py`)**: `repeat(elem, n)` yields an object $n$ times; `starmap(func, tuples)` calls `func(*item)`; `tee(it, 2)` duplicates an iterator; and `zip_longest(*iterables, fillvalue=...)` pairs sequences without truncating shorter iterables.

---

## 🧠 Beginner tip

Remember that `itertools.groupby()` is **consecutive**, not global. Unlike SQL's `GROUP BY` or Pandas `.groupby()`, Python's `groupby()` only merges items that appear consecutively next to each other. If your dataset contains unsorted duplicate keys (e.g. `['cat', 'dog', 'cat']`), you will get two separate `'cat'` groups unless you sort the data by key first (`data.sort(key=...)`).

---

## 📊 Where this is used in Data Science

- **Hyperparameter Grid Search**: Machine learning pipelines compute Cartesian parameter combinations using `product(learning_rates, batch_sizes, optimizers)` to evaluate all model hyperparameter configurations without writing nested `for` loops.
- **Batch Processing & Padded Data Streaming**: In deep learning batching, sequence data often has uneven lengths; `zip_longest(*batches, fillvalue=0)` pads batches of tokens or vectors to uniform matrix dimensions before tensor conversion.
- **Cumulative Financial & Time-Series Metrics**: `accumulate()` computes running portfolio balances, cumulative cash flows, and cumulative returns across millions of transaction records in constant memory.

---

## 🛠️ Code Examples

### Cartesian Products for Grid Search
```python
from itertools import product

learning_rates = [0.01, 0.001]
batch_sizes = [32, 64]
optimizers = ["adam", "sgd"]

# Generates all 8 combinations lazily
grid = list(product(learning_rates, batch_sizes, optimizers))
print("Total configurations:", len(grid))
print("First config:", grid[0])  # (0.01, 32, 'adam')
```

### Cumulative Running Totals with `accumulate`
```python
from itertools import accumulate

monthly_sales = [1200, 1500, 1100, 1800]
running_totals = list(accumulate(monthly_sales))
print("Running sales:", running_totals)  # [1200, 2700, 3800, 5600]
```

### Safe Infinite Stream Sampling with `islice` and `count`
```python
from itertools import count, islice

# Generate numbers starting at 100 with step of 15
even_stream = count(100, 15)

# Lazily pull only the first 4 numbers without an infinite loop
sample = list(islice(even_stream, 4))
print("Sampled numbers:", sample)  # [100, 115, 130, 145]
```

---

## ⏭️ What's Next

Master first-class functions, closures, decorators, and function transformations in **[Chapter 19 — Functional Tools](../chapter_19_functional_tools/README.md)**!
