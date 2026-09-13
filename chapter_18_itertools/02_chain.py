"""
📚 Topic: chain

This script demonstrates chain from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import chain

# ============================================================
# 1. BASIC CHAIN
# ============================================================
print("=" * 60)
print("1. BASIC CHAIN")
print("=" * 60)

first = [1, 2, 3]
second = [4, 5, 6]
third = [7, 8, 9]

print("Chained:", list(chain(first, second, third)))


# ============================================================
# 2. CHAIN FROM ITERABLE
# ============================================================
print("\n" + "=" * 60)
print("2. CHAIN FROM ITERABLE")
print("=" * 60)

groups = [[1, 2], [3, 4], [5, 6]]
print("Groups:", groups)
print("Chained:", list(chain.from_iterable(groups)))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("chain examples completed!")
print("=" * 60)
