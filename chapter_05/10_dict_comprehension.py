"""
📚 Topic: Dictionary Comprehensions

This script demonstrates dictionary comprehensions using for loops, list
comprehensions, dictionary comprehensions and imports.

💡 Key points:
    1️⃣ the basic syntax for dictionary comprehensions
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    dictionary comprehensions affects the result.
"""


# ============================================================
# 1. BASIC DICTIONARY COMPREHENSION
# ============================================================
import time
import math
print("=" * 60)
print("1. BASIC DICTIONARY COMPREHENSION")
print("=" * 60)

# Syntax: {key_expr: value_expr for item in iterable}

# Create a dictionary of squares
squares: dict[int, int] = {x: x**2 for x in range(1, 6)}
print(f"  Squares: {squares}")

# Create a dictionary of cube roots
cubes: dict[int, int] = {x: x**3 for x in range(1, 6)}
print(f"  Cubes: {cubes}")

# Map strings to their lengths
words = ["apple", "banana", "cherry", "date"]
word_lengths: dict[str, int] = {word: len(word) for word in words}
print(f"  Word lengths: {word_lengths}")


# ============================================================
# 2. DICTIONARY COMPREHENSION WITH CONDITION (FILTER)
# ============================================================
print("\n" + "=" * 60)
print("2. DICTIONARY COMPREHENSION WITH CONDITION")
print("=" * 60)

# Syntax: {key_expr: value_expr for item in iterable if condition}

# Even squares only
even_squares: dict[int, int] = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"  Even squares: {even_squares}")

# Words with length > 5
long_words: dict[str, int] = {w: len(w) for w in words if len(w) > 5}
print(f"  Long words (>5 chars): {long_words}")

# Numbers and their parity
parity: dict[int, str] = {x: "even" if x % 2 == 0 else "odd" for x in range(1,
                                                                            6)}
print(f"  Parity: {parity}")


# ============================================================
# 3. DICTIONARY COMPREHENSION FROM TWO ITERABLES (ZIP)
# ============================================================
print("\n" + "=" * 60)
print("3. DICTIONARY COMPREHENSION WITH ZIP")
print("=" * 60)

names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [25, 30, 35, 28]
cities = ["NYC", "LA", "Chicago", "Houston"]

# Basic zip comprehension
name_to_age: dict[str, int] = {name: age for name, age in zip(names, ages)}
print(f"  Name to age: {name_to_age}")

# Zip with condition
adults: dict[str, int] = {name: age for name, age in zip(names, ages) if age >=
                          30}
print(f"  Adults (age >= 30): {adults}")

# Zip with transformation
name_city_upper: dict[str, str] = {n: c.upper() for n, c in zip(names, cities)}
print(f"  Name to city (upper): {name_city_upper}")

# Enumerate with zip
indexed_ages: dict[int, str] = {
    i: f"{n} is {a}" for i, (n, a) in enumerate(zip(names, ages))
}
print(f"  Indexed ages: {indexed_ages}")


# ============================================================
# 4. DICTIONARY COMPREHENSION WITH ENUMERATE
# ============================================================
print("\n" + "=" * 60)
print("4. DICTIONARY COMPREHENSION WITH ENUMERATE")
print("=" * 60)

fruits = ["apple", "banana", "cherry", "date"]

# Index to fruit
fruit_by_index: dict[int, str] = {i: fruit for i, fruit in enumerate(fruits)}
print(f"  Fruit by index: {fruit_by_index}")

# Index to uppercase fruit
fruit_upper: dict[int, str] = {i: fruit.upper() for i, fruit in
                               enumerate(fruits)}
print(f"  Uppercase fruits: {fruit_upper}")

# Index to fruit (filtered)
fruit_filtered: dict[int, str] = {i: f for i, f in enumerate(fruits) if "a" in
                                  f}
print(f"  Fruits containing 'a': {fruit_filtered}")


# ============================================================
# 5. NESTED DICTIONARY COMPREHENSION
# ============================================================
print("\n" + "=" * 60)
print("5. NESTED DICTIONARY COMPREHENSION")
print("=" * 60)

# Multiplication table as nested dict
mult_table: dict[int, dict[int, int]] = {
    i: {j: i * j for j in range(1, 6)} for i in range(1, 6)
}
print("  Multiplication table:")
for key, val in mult_table.items():
    print(f"    {key}: {val}")

# Flatten a nested dict
nested: dict[str, dict[str, int]] = {
    "A": {"x": 1, "y": 2},
    "B": {"x": 3, "y": 4},
}
flat: dict[tuple[str, str], int] = {
    (outer, inner): value
    for outer, inner_dict in nested.items()
    for inner, value in inner_dict.items()
}
print(f"  Flattened nested: {flat}")


# ============================================================
# 6. TRANSFORMING EXISTING DICTIONARIES
# ============================================================
print("\n" + "=" * 60)
print("6. TRANSFORMING EXISTING DICTIONARIES")
print("=" * 60)

original: dict[str, int] = {"a": 1, "b": 2, "c": 3, "d": 4}

# Swap keys and values
swapped: dict[int, str] = {v: k for k, v in original.items()}
print(f"  Original: {original}")
print(f"  Swapped (k<->v): {swapped}")

# Filter and transform
doubled_evens: dict[str, int] = {k: v * 2 for k, v in original.items() if v % 2
                                 == 0}
print(f"  Doubled evens: {doubled_evens}")

# Convert keys to uppercase
upper_keys: dict[str, int] = {k.upper(): v for k, v in original.items()}
print(f"  Upper keys: {upper_keys}")

# String representations
stringified: dict[str, str] = {k: f"value_{v}" for k, v in original.items()}
print(f"  Stringified values: {stringified}")


# ============================================================
# 7. DICTIONARY COMPREHENSION WITH FUNCTIONS
# ============================================================
print("\n" + "=" * 60)
print("7. DICTIONARY COMPREHENSION WITH FUNCTIONS")
print("=" * 60)

# Using string methods
words_list: list[str] = ["hello", "world", "python", "code"]

# First letter -> word
first_letter_map: dict[str, str] = {w[0]: w for w in words_list}
print(f"  First letter map: {first_letter_map}")

# Char count for each word
char_counts: dict[str, int] = {w: len(set(w)) for w in words_list}
print(f"  Unique char counts: {char_counts}")

# Using conditional expressions
parity_status: dict[int, str] = {
    x: "positive" if x > 0 else "zero" if x == 0 else "negative" for x in
    range(-2, 3)
}
print(f"  Parity status: {parity_status}")


# ============================================================
# 8. DICTIONARY COMPREHENSION WITH WALRUS OPERATOR (:=)
# ============================================================
print("\n" + "=" * 60)
print("8. DICTIONARY COMPREHENSION WITH WALRUS OPERATOR")
print("=" * 60)


# Compute value once and reuse it
results: dict[int, tuple[float, float]] = {
    x: (y := math.sqrt(x), y**2) for x in range(1, 6)
}
print(f"  Square roots and squares: {results}")

# Filter using computed value
expensive_data: dict[int, int] = {x: (val := x**3) for x in range(1, 11) if val
                                  > 100}
print(f"  Cubes > 100: {expensive_data}")


# ============================================================
# 9. CONDITIONAL VALUE (TERNARY IN COMPREHENSION)
# ============================================================
print("\n" + "=" * 60)
print("9. CONDITIONAL VALUES")
print("=" * 60)

# Different values based on condition
classifications: dict[int, str] = {x: "high" if x > 5 else "low" for x in
                                   range(1, 11)}
print(f"  Classifications: {classifications}")

# Multi-level conditional
grade_map: dict[int, str] = {
    score: "A"
    if score >= 90
    else "B"
    if score >= 80
    else "C"
    if score >= 70
    else "D"
    if score >= 60
    else "F"
    for score in [95, 82, 75, 65, 50]
}
print(f"  Grades: {grade_map}")


# ============================================================
# 10. PRACTICAL EXAMPLES
# ============================================================
print("\n" + "=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Invert a dictionary (group by value)
scores: dict[str, int] = {"Alice": 85, "Bob": 92, "Charlie": 85, "Diana": 92,
                          "Eve": 78}
by_score: dict[int, list[str]] = {
    score: [name for name, s in scores.items() if s == score]
    for score in set(scores.values())
}
print(f"  Grouped by score: {by_score}")

# Example 2: Count character frequency
text: str = "dictionary comprehension"
char_freq: dict[str, int] = {char: text.count(char) for char in set(text)}
print(f"  Character frequency in '{text}': {char_freq}")

# Example 3: Convert two lists to dictionary with default
keys_list: list[str] = ["name", "age", "city"]
values_list: list[str] = ["Frank", "30", "Boston"]
person_dict: dict[str, str] = {k: v for k, v in zip(keys_list, values_list)}
print(f"  Person dict: {person_dict}")

# Example 4: ASCII values
ascii_map: dict[str, int] = {chr(i): i for i in range(65, 70)}
print(f"  ASCII map: {ascii_map}")

# Example 5: From range with step
positions: dict[int, str] = {i: f"position_{i}" for i in range(0, 20, 5)}
print(f"  Positions: {positions}")


# ============================================================
# 11. DICTIONARY COMPREHENSION VS DICT() CONSTRUCTOR
# ============================================================
print("\n" + "=" * 60)
print("11. COMPREHENSION vs DICT() CONSTRUCTOR")
print("=" * 60)

# Using dict() constructor with keyword args (limited)
dict_constructor: dict[str, int] = dict(a=1, b=2, c=3)

# Using comprehension (more flexible)
dict_comp: dict[str, int] = {k: ord(k) - ord("a") + 1 for k in "abc"}

print(f"  dict() constructor: {dict_constructor}")
print(f"  Comprehension:      {dict_comp}")

# From list of tuples
pairs: list[tuple[str, int]] = [("x", 1), ("y", 2), ("z", 3)]
from_pairs_comp: dict[str, int] = {k: v for k, v in pairs}
from_pairs_ctor: dict[str, int] = dict(pairs)
print(f"  From pairs (comp):  {from_pairs_comp}")
print(f"  From pairs (ctor):  {from_pairs_ctor}")


# ============================================================
# 12. PERFORMANCE EXAMPLE
# ============================================================
print("\n" + "=" * 60)
print("12. PERFORMANCE CONSIDERATION")
print("=" * 60)


# Large dictionary creation - comprehension is faster than loops
size: int = 1_000_000

# Method 1: Comprehension (fast)
start: float = time.perf_counter()
dict_comp_large: dict[int, int] = {i: i**2 for i in range(size)}
comp_time: float = time.perf_counter() - start

# Method 2: Loop (slower)
start = time.perf_counter()
dict_loop_large: dict[int, int] = {}
for i in range(size):
    dict_loop_large[i] = i**2
loop_time: float = time.perf_counter() - start

print(f"  Comprehension time: {comp_time:.4f}s")
print(f"  Loop time:          {loop_time:.4f}s")
print(f"  Comprehension is ~{loop_time / comp_time:.2f}x faster")


print("\n" + "=" * 60)
print("Dictionary comprehension examples completed!")
print("=" * 60)
