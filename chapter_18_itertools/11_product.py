"""
📚 Topic: product

This script demonstrates product from Python's itertools module.

💡 Key points:
    1. Basic usage
    2. Important arguments
    3. Practical iterator example

🧠 Beginner tip:
    Run this file and change the input values to see how
    the iterator behaves.
"""


from itertools import product

# ============================================================
# 1. BASIC PRODUCT
# ============================================================
print("=" * 60)
print("1. BASIC PRODUCT")
print("=" * 60)

colors = ["red", "blue"]
sizes = ["S", "M"]
print("Products:", list(product(colors, sizes)))


# ============================================================
# 2. PRODUCT WITH REPEAT
# ============================================================
print("\n" + "=" * 60)
print("2. PRODUCT WITH REPEAT")
print("=" * 60)

print("Products:", list(product([1, 2], repeat=2)))


# ============================================================
# COMPLETION
# ============================================================
print("\n" + "=" * 60)
print("product examples completed!")
print("=" * 60)
