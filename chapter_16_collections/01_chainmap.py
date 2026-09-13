"""
📚 Topic: ChainMap

This script demonstrates ChainMap from Python's collections module.

💡 Key points:
    1. Creating a ChainMap
    2. Accessing values
    3. Iterating over a ChainMap
    4. Adding a new child mapping
    5. Accessing parent mappings

🧠 Beginner tip:
    Run this file section by section and change one dictionary
    to understand how ChainMap searches through its mappings.
"""

from collections import ChainMap


# ============================================================
# 1. BASIC CHAINMAP
# ============================================================

print("=" * 60)
print("1. BASIC CHAINMAP")
print("=" * 60)

fruits_dict = {
    "apple": "red",
    "banana": "yellow",
    "pear": "green",
    "orange": "orange",
}

person_dict = {
    "John": "apple",
    "Alex": "Oranges",
    "Samantha": "pears",
}

chain = ChainMap(fruits_dict, person_dict)

print("Fruits:", fruits_dict)
print("People:", person_dict)
print("Chain:", chain)


# ============================================================
# 2. ACCESS VALUES
# ============================================================

print("\n" + "=" * 60)
print("2. ACCESS VALUES")
print("=" * 60)

print("apple:", chain["apple"])
print("orange:", chain["orange"])
print("Samantha:", chain["Samantha"])


# ============================================================
# 3. ITERATE OVER CHAINMAP
# ============================================================

print("\n" + "=" * 60)
print("3. ITERATE OVER CHAINMAP")
print("=" * 60)

for key, value in chain.items():
    print(f"{key} --> {value}")


# ============================================================
# 4. NEW CHILD
# ============================================================

print("\n" + "=" * 60)
print("4. NEW CHILD")
print("=" * 60)

vegetables_dict = {
    "tomato": "red",
    "cucumber": "green",
}

chain = chain.new_child(vegetables_dict)

print("Vegetables:", vegetables_dict)
print("Updated chain:", chain)


# ============================================================
# 5. KEYS
# ============================================================

print("\n" + "=" * 60)
print("5. KEYS")
print("=" * 60)

print("Keys:", list(chain.keys()))


# ============================================================
# 6. PARENTS
# ============================================================

print("\n" + "=" * 60)
print("6. PARENTS")
print("=" * 60)

print("Parent mappings:", chain.parents)


# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 60)
print("ChainMap examples completed!")
print("=" * 60)
