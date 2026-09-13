# 🐍 Chapter 16 — Collections Module: Specialized Container Data Types 📦

Welcome to Chapter 16! Python's built-in general containers (`dict`, `list`, `set`, `tuple`) are fantastic, but real-world engineering often requires specialized data structures. The standard library's `collections` module provides specialized, high-performance alternatives designed to make common data-processing patterns cleaner and drastically faster.

---

## 📂 Files in This Chapter

| # | File | Topic | Quick Peek |
|---|---|---|---|
| 01 | `01_chainmap.py` | `ChainMap` | Linking multiple dictionaries into a single lookup view |
| 02 | `02_counter.py` | `Counter` | Fast frequency and tally counter for hashable objects |
| 03 | `03_defaultdict.py` | `defaultdict` | Dictionaries providing default factories for missing keys |
| 04 | `04_namedtuple_via_collections.py` | `namedtuple` | Lightweight object-like tuples with named fields |
| 05 | `05_deque.py` | `deque` | $O(1)$ Double-Ended Queue with fast left/right operations |

---

## 🔗 1. `ChainMap`: Multi-Dictionary Views (`01_chainmap.py`)

`ChainMap` groups multiple dictionaries into a single mapping without copying all their contents into memory. Lookups search through the dictionaries in the order they were provided:

```python
from collections import ChainMap

defaults = {"theme": "light", "show_tips": True, "font_size": 14}
user_settings = {"theme": "dark", "font_size": 16}

config = ChainMap(user_settings, defaults)

print(config["theme"])      # 'dark' (found in user_settings first)
print(config["show_tips"])  # True   (falls back to defaults)
```

---

## 📊 2. `Counter`: Effortless Frequency Counting (`02_counter.py`)

`Counter` tallies elements automatically and provides convenient methods like `.most_common()`:

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)

print(counts)                   # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counts["banana"])         # 2
print(counts.most_common(1))    # [('apple', 3)]
```

---

## 🪄 3. `defaultdict`: Never Face `KeyError` Again (`03_defaultdict.py`)

`defaultdict` takes a callable factory function (such as `list`, `int`, or `set`) that supplies a default value whenever a nonexistent key is accessed:

```python
from collections import defaultdict

# Grouping items by category
inventory = defaultdict(list)
inventory["fruits"].append("apple")
inventory["fruits"].append("banana")
inventory["veggies"].append("carrot")

print(dict(inventory))
# {'fruits': ['apple', 'banana'], 'veggies': ['carrot']}

# Frequency counting with int default
tally = defaultdict(int)
tally["clicks"] += 1
print(tally["clicks"])  # 1
```

---

## 🏷️ 4. `namedtuple`: Readable Tuples (`04_namedtuple_via_collections.py`)

`namedtuple` assigns meaning to each position in a tuple, allowing more readable, self-documenting code:

```python
from collections import namedtuple

Color = namedtuple("Color", ["r", "g", "b"])
cyan = Color(r=0, g=255, b=255)

print(cyan.r, cyan.g, cyan.b)  # 0 255 255
print(cyan[0])                 # 0 (still indexable!)
```

---

## ⚡ 5. `deque`: Double-Ended Queues (`05_deque.py`)

A standard Python `list` has $O(n)$ time complexity for insertions or removals at the beginning (`list.pop(0)` or `list.insert(0, x)`). A `deque` provides lightning-fast **$O(1)$** performance from **both ends**:

```python
from collections import deque

dq = deque([1, 2, 3])

# Fast appends and pops on both ends
dq.append(4)         # Add to right
dq.appendleft(0)     # Add to left -> deque([0, 1, 2, 3, 4])
dq.pop()             # Remove 4
dq.popleft()         # Remove 0

# Bounded ring-buffer with maxlen
history = deque(maxlen=3)
for i in range(5):
    history.append(i)
print(history)       # deque([2, 3, 4], maxlen=3) -> oldest dropped!
```

---

## 🎯 Cheat Sheet

| Type | When to Use | Key Superpower |
|---|---|---|
| `ChainMap` | Merging defaults with overrides / scopes | Zero-copy multi-dict lookup |
| `Counter` | Counting occurrences, finding top N items | `.most_common()`, arithmetic math |
| `defaultdict` | Grouping, graph adjacencies, tallying | Auto-initializes missing keys |
| `namedtuple` | Fixed structured records, coordinates | Field name access without class boilerplate |
| `deque` | FIFO Queues, sliding windows, ring buffers | $O(1)$ appends and pops from left and right |

---

## ⏭️ What's Next?
Next, explore memory-efficient data processing with **[Chapter 17 — Iterators & Generators](../chapter_17_iterators_generators/README.md)**!
