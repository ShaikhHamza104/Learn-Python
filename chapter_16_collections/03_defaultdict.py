"""
📚 Topic: defaultdict

This script demonstrates defaultdict from Python's collections module.

💡 Key points:
    1. Normal dictionary lookup
    2. get() method
    3. Creating a defaultdict
    4. Default values
    5. Counting values with defaultdict

🧠 Beginner tip:
    A defaultdict automatically creates a default value when
    a missing key is accessed.
"""

from collections import defaultdict


# ============================================================
# 1. NORMAL DICTIONARY
# ============================================================

print("=" * 60)
print("1. NORMAL DICTIONARY")
print("=" * 60)

person_dict = {
    "John": "apple",
    "Alex": "Oranges",
    "Samantha": "pears",
}

print("Dictionary:", person_dict)
print("John:", person_dict["John"])


# ============================================================
# 2. MISSING KEY
# ============================================================

print("\n" + "=" * 60)
print("2. MISSING KEY")
print("=" * 60)

# Direct access to a missing key raises KeyError.

try:
    print(person_dict["James"])
except KeyError:
    print("James is not present in the dictionary.")


# ============================================================
# 3. GET METHOD
# ============================================================

print("\n" + "=" * 60)
print("3. GET METHOD")
print("=" * 60)

print("John:", person_dict.get("John"))
print("James:", person_dict.get("James"))


# ============================================================
# 4. BASIC DEFAULTDICT
# ============================================================

print("\n" + "=" * 60)
print("4. BASIC DEFAULTDICT")
print("=" * 60)

default_dict = defaultdict(lambda: "Missing")

print("Defaultdict:", default_dict)
print("As dictionary:", dict(default_dict))


# ============================================================
# 5. DEFAULT VALUE
# ============================================================

print("\n" + "=" * 60)
print("5. DEFAULT VALUE")
print("=" * 60)

print("A:", default_dict["A"])
print("B:", default_dict["B"])

print("Updated dictionary:", dict(default_dict))


# ============================================================
# 6. DEFAULTDICT FOR COUNTING
# ============================================================

print("\n" + "=" * 60)
print("6. DEFAULTDICT FOR COUNTING")
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

count_dict = defaultdict(lambda: 0)

for name in names:
    count_dict[name] += 1

print("Counts:", dict(count_dict))


# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 60)
print("defaultdict examples completed!")
print("=" * 60)
