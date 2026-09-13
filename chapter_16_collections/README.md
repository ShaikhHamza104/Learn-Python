# 📚 Topic: Collections Module

Python's built-in general containers (`dict`, `list`, `set`, `tuple`) form the foundation of everyday scripting. However, specialized workflows demand containers optimized for performance and convenience. The standard library's `collections` module provides dedicated data structures including `ChainMap`, `Counter`, `defaultdict`, `namedtuple`, and `deque` to streamline common algorithms and eliminate boilerplate code.

---

## 📂 What's in this folder

| File | What it teaches |
| --- | --- |
| `01_chainmap.py` | Grouping multiple dictionaries into a single lookup view, `.new_child()`, and `.parents` |
| `02_counter.py` | Fast frequency counting, iterating via `.elements()`, and top-rank extraction with `.most_common()` |
| `03_defaultdict.py` | Eliminating `KeyError` exceptions using factory callables and tallying frequencies |
| `04_namedtuple_via_collections.py` | Creating immutable object-like tuples with field names, `._asdict()`, and `._replace()` |
| `05_deque.py` | Double-ended queues with $O(1)$ push/pop operations from both ends and fixed-size ring buffers with `maxlen` |

---

## 💡 Key points

1. **Multi-Scope Dictionary Views (`01_chainmap.py`)**: `ChainMap` searches across multiple dictionaries sequentially without copying their contents into a new dictionary. Adding overrides with `.new_child()` creates child scopes, while `.parents` returns the underlying parent mappings.
2. **Frequency Counting & Rankings (`02_counter.py`)**: `Counter` automatically tallies occurrences of hashable items in an iterable. `.elements()` yields elements repeated by their frequency count, and `.most_common(n)` retrieves the top $n$ most frequent items sorted by count.
3. **Automatic Key Initialization (`03_defaultdict.py`)**: `defaultdict(factory)` invokes the provided callable (such as `lambda: "Missing"` or `lambda: 0`) when an accessed key is absent, avoiding explicit existence checks or handling `KeyError`.
4. **Readable Immutable Records (`04_namedtuple_via_collections.py`)**: `namedtuple("Point", "x y")` generates tuple subclasses accessible via named attributes (`p.x`, `p.y`) while retaining positional indexing, tuple immutability, and providing helper methods like `._asdict()` and `._replace()`.
5. **High-Speed Double-Ended Queues (`05_deque.py`)**: Unlike Python lists where inserting or removing from the left is $O(n)$, `deque` performs `appendleft()` and `popleft()` in $O(1)$ time. Setting `maxlen` converts the deque into a bounded FIFO buffer where old items are automatically evicted when capacity is reached.

---

## 🧠 Beginner tip

When implementing sliding windows or rolling logs, always use `deque(maxlen=N)` instead of a list. When appending to a full `deque(maxlen=N)`, the oldest element from the opposing end is discarded in $O(1)$ time without requiring manual `.pop(0)` calls that re-index the entire list.

---

## 📊 Where this is used in Data Science

- **NLP Vocabulary Building & N-Gram Frequencies**: `Counter` is the standard tool for counting word and token frequencies across text corpora, generating term frequency tables, and pruning rare vocabulary words with `.most_common()`.
- **Feature Grouping & Adjacency Graphs**: `defaultdict(list)` and `defaultdict(set)` group customer transactions by user ID or build graph adjacency maps for recommendation algorithms without needing verbose `.setdefault()` checks.
- **Sliding Window Feature Engineering**: Time-series preprocessing pipelines use `deque(maxlen=window_size)` to compute moving averages, rolling standard deviations, and recent sensor history buffers with minimal memory overhead.

---

## 🛠️ Code Examples

### Vocabulary Frequency Tally with `Counter`
```python
from collections import Counter

tokens = ["python", "data", "ml", "python", "ai", "data", "python"]
word_counts = Counter(tokens)

print("Top word:", word_counts.most_common(1))  # [('python', 3)]
print("Count of 'data':", word_counts["data"])   # 2
```

### Grouping Records with `defaultdict`
```python
from collections import defaultdict

transactions = [
    ("Alice", 120),
    ("Bob", 80),
    ("Alice", 45),
    ("Charlie", 200),
]

user_orders = defaultdict(list)
for customer, amount in transactions:
    user_orders[customer].append(amount)

print(dict(user_orders))
# {'Alice': [120, 45], 'Bob': [80], 'Charlie': [200]}
```

### Bounded Buffer with `deque`
```python
from collections import deque

# Keep only the last 3 incoming sensor readings
recent_readings = deque(maxlen=3)
for reading in [21.5, 22.0, 22.4, 23.1, 22.8]:
    recent_readings.append(reading)

print("Recent buffer:", list(recent_readings))  # [22.4, 23.1, 22.8]
```

---

## ⏭️ What's Next

Learn how to write memory-efficient streaming pipelines using custom iterators and generator functions in **[Chapter 17 — Iterators & Generators](../chapter_17_iterators_generators/README.md)**!
