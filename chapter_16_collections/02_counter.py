"""
📚 Topic: Counter

This script demonstrates Counter from Python's collections module.

💡 Key points:
    1. Creating a Counter
    2. Counting elements
    3. Iterating over elements
    4. Finding the most common elements

🧠 Beginner tip:
    Change the values in the list and run the file again
    to see how the Counter changes.
"""

from collections import Counter


# ============================================================
# 1. BASIC COUNTER
# ============================================================

print("=" * 60)
print("1. BASIC COUNTER")
print("=" * 60)

names = [
    "ankit",
    "akash",
    "hemant",
    "neha",
    "akash",
    "akash",
    "ankit",
    "neha",
    "akash",
]

print("Names:", names)

count = Counter(names)

print("Counter:", count)


# ============================================================
# 2. ELEMENTS
# ============================================================

print("\n" + "=" * 60)
print("2. ELEMENTS")
print("=" * 60)

# elements() returns each element according to its count.

for element in count.elements():
    print(element)


# ============================================================
# 3. MOST COMMON
# ============================================================

print("\n" + "=" * 60)
print("3. MOST COMMON")
print("=" * 60)

print("Top 2:", count.most_common(2))


# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 60)
print("Counter examples completed!")
print("=" * 60)
