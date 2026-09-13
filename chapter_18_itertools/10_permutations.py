"""
📚 Topic: permutations

This script demonstrates permutations from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import permutations

# ============================================================
# 1. BASIC PERMUTATIONS
# ============================================================
print("=" * 60)
print("1. BASIC PERMUTATIONS")
print("=" * 60)

values = [1, 2, 3]
print("Permutations:", list(permutations(values)))


# ============================================================
# 2. PERMUTATIONS WITH LENGTH
# ============================================================
print("\n" + "=" * 60)
print("2. PERMUTATIONS WITH LENGTH")
print("=" * 60)

print("Length 2:", list(permutations(values, 2)))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("permutations examples completed!")
print("=" * 60)
