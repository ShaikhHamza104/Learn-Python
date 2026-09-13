# 📚 Topic: Lists and Tuples

Lists and tuples are Python's fundamental ordered collection types. Lists are mutable sequences that can be modified, appended to, sorted, and reorganized in-place. Tuples are immutable sequences designed for fixed, read-only data. This chapter covers list initialization, CRUD manipulation, core methods, single-element and multi-element tuples, indexed iteration with `enumerate()`, method discovery using `dir()`, list comprehensions, and self-documenting records using `collections.namedtuple`.

## 📂 What's in this folder

| File | What it teaches |
|---|---|
| `01_list.py` | List creation using square brackets `[]` and the `list()` constructor, supporting mixed types and empty list creation. |
| `02_operation_list.py` | CRUD operations on lists: Creating, Reading with forward/negative indices, Updating in-place, and Deleting elements with `del`. |
| `03_list_method.py` | Essential list methods: `.append()`, `.insert()`, `.extend()`, `.remove()`, `.pop()`, `del`, `.sort()`, `.reverse()`, `.copy()`, `.clear()`, `.count()`, and `.index()`. |
| `04_tuple.py` | Tuple creation, indexing, immutability checks with `try/except`, and the trailing comma rule for single-element tuples `(1,)`. |
| `05_operation_tuple.py` | Joining tuples with concatenation (`+`) and repeating elements with repetition (`*`). |
| `06_tuple_method.py` | Inspecting tuples using `len()`, counting occurrences with `.count()`, and locating positions with `.index()`. |
| `07_enumerate.py` | Iterating through collections using `enumerate()` to access both index and item simultaneously. |
| `08_dir_method.py` | Introspection with `dir()` to discover all available attributes and methods of a list object. |
| `09_list_comprehension.py` | Concise syntax for generating and filtering lists using list comprehensions with `range()` and conditionals. |
| `10_namedtuple.py` | Creating structured, immutable records with `collections.namedtuple`, attribute access, dictionary conversion (`_asdict()`), and field replacement (`_replace()`). |

## 💡 Key points

1. **Mutability vs. Immutability**: Lists can be updated in-place (`li[0] = 99`), whereas tuples cannot be altered after creation (attempting `t[0] = 99` raises `TypeError`).
2. **Single-Element Tuples**: A single value in parentheses `(1)` is evaluated as an integer; a trailing comma `(1,)` is mandatory to define a single-element tuple.
3. **In-Place List Methods**: Methods such as `.sort()`, `.reverse()`, and `.append()` modify the list directly in memory and return `None`.
4. **List Comprehensions**: Provide a clear, pythonic one-liner syntax (`[expr for item in iterable if condition]`) that replaces verbose `for` loop construction.
5. **Named Tuples**: `collections.namedtuple` creates memory-efficient tuple subclasses that allow accessing fields by name (`point.x`) as well as numeric indices (`point[0]`).

## 🧠 Beginner tip

Watch out for the single-element tuple pitfall! Writing `t = (5)` does not create a tuple—it evaluates to an ordinary integer `5`. You must write `t = (5,)` with a trailing comma for Python to recognize it as a tuple.

## 📊 Where this is used in Data Science

Lists and tuples are central to Python data pipelines. Lists collect raw feature values, query results, and file records prior to converting them into Pandas Series or NumPy arrays. Tuples represent fixed metadata such as DataFrame dimensions `df.shape -> (rows, cols)`, database query rows, and immutable coordinate pairs. List comprehensions are used daily for batch string cleaning, filtering outlier records, and quick feature extraction.

## 🛠️ Code Examples

### List Operations and Methods (`01_list.py` - `03_list_method.py`)
```python
numbers = [1, 2, 3]
numbers.append(10)          # [1, 2, 3, 10]
numbers.insert(0, 0)        # [0, 1, 2, 3, 10]
numbers[1] = 99             # In-place update
popped = numbers.pop(1)     # Removes and returns 99
numbers.sort(reverse=True)  # In-place descending sort
```

### Tuples and Immutability (`04_tuple.py` - `06_tuple_method.py`)
```python
single = (42,)              # Trailing comma required
coords = (10, 20, 30, 20)
print(coords[0])            # 10
print(coords.count(20))     # 2
# coords[0] = 99            # Raises TypeError!
```

### List Comprehension (`09_list_comprehension.py`)
```python
evens = [x for x in range(10, 41) if x % 2 == 0]
odds = [x for x in range(10, 21) if x % 2 != 0]
```

### Enumerate and Named Tuples (`07_enumerate.py`, `10_namedtuple.py`)
```python
from collections import namedtuple

for index, element in enumerate(["Rohan", "Rahol"]):
    print(index, element)

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(f"X: {p.x}, Y: {p.y}, As Dict: {p._asdict()}")
```

## 🏋️ Practice Exercises

Sharpen your skills on lists, tuples, and data collection problems:
- [Chapter 04 Exercises](../chapter_04_lists_tuples_exercises/README.md)

## ⏭️ What's Next

- [Chapter 05 - Dictionaries and Sets](../chapter_05_dicts_sets/README.md)
