"""
📚 Topic: namedtuple

This script demonstrates namedtuple from Python's collections module.

💡 Key points:
    1. Creating a namedtuple
    2. Creating namedtuple objects
    3. _asdict()
    4. _fields
    5. Accessing fields
    6. _replace()
    7. Identity of namedtuple objects

🧠 Beginner tip:
    A namedtuple behaves like a tuple but gives its fields
    readable names.
"""

from collections import namedtuple


# ============================================================
# 1. BASIC NAMEDTUPLE
# ============================================================

print("=" * 60)
print("1. BASIC NAMEDTUPLE")
print("=" * 60)

Point = namedtuple("Point", "x y")

print("Point type:", Point)


# ============================================================
# 2. CREATE A NAMEDTUPLE
# ============================================================

print("\n" + "=" * 60)
print("2. CREATE A NAMEDTUPLE")
print("=" * 60)

point_one = Point(x=6, y=4)

print("Point:", point_one)


# ============================================================
# 3. _ASDICT()
# ============================================================

print("\n" + "=" * 60)
print("3. _ASDICT()")
print("=" * 60)

print("Dictionary:", point_one._asdict())


# ============================================================
# 4. _FIELDS
# ============================================================

print("\n" + "=" * 60)
print("4. _FIELDS")
print("=" * 60)

print("Fields:", point_one._fields)


# ============================================================
# 5. ACCESS FIELDS
# ============================================================

print("\n" + "=" * 60)
print("5. ACCESS FIELDS")
print("=" * 60)

print("x:", point_one.x)
print("y:", point_one.y)


# ============================================================
# 6. _REPLACE()
# ============================================================

print("\n" + "=" * 60)
print("6. _REPLACE()")
print("=" * 60)

point_two = point_one._replace(y=10)

print("Original:", point_one)
print("Updated:", point_two)


# ============================================================
# 7. IDENTITY
# ============================================================

print("\n" + "=" * 60)
print("7. IDENTITY")
print("=" * 60)

print("point_one id:", id(point_one))
print("point_two id:", id(point_two))

print("Same object:", point_one is point_two)


# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 60)
print("namedtuple examples completed!")
print("=" * 60)
