"""
📚 Topic: Chapter 05 Exercise - Problem 9

Demonstrate that a mutable list cannot be placed inside a set.

💡 Key points:
    1️⃣ Set elements must be hashable and immutable
    2️⃣ Python lists are mutable and unhashable (`TypeError: unhashable type`)
    3️⃣ Tuples can be used as set elements instead of lists
"""
# ❌ A list cannot be an element of a set because lists are mutable
# and therefore unhashable.
try:
    s = {8, 7, 12, "Harry", [1, 2]}
    print(s)
except TypeError as error:
    print(f"TypeError caught as expected: {error}")
    # ✅ Tuples can be used instead because they are immutable:
    valid_set = {8, 7, 12, "Harry", (1, 2)}
    print(f"Valid set with tuple: {valid_set}")
