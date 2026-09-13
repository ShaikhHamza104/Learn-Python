"""
📚 Topic: Opration Set

This script demonstrates opration set using basic Python syntax.

💡 Key points:
    1️⃣ the basic syntax for opration set
    2️⃣ how basic Python syntax fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    opration set affects the result.
"""


# 📦 Creating the first set
# Notice that 1 appears twice, but a set keeps only one copy.
s1 = {1, 2, 3, 4, 90}


# 📦 Creating the second set
s2 = {90, 1, 2, 5, 67, 8, 91}


# 🔗 Union of two sets
# union() combines all unique elements from both sets.
#
# Common elements are included only once.
print(s1.union(s2))

# Output:
# {1, 2, 3, 4, 5, 67, 8, 90, 91}


# 🤝 Intersection of two sets
# intersection() returns only the elements
# that are present in BOTH sets.
#
# Here, 1, 2 and 90 are common in s1 and s2.
print(s1.intersection(s2))

# Output:
# {1, 2, 90}


# ➖ Difference between two sets
# difference() returns the elements that are present
# in s1 but NOT present in s2.
#
# Here, 3 and 4 are only present in s1.
print(s1.difference(s2))

# Output:
# {3, 4}


# 🔍 Check if s1 is a subset of s2
# issubset() checks whether every element of s1
# is also present in s2.
#
# s1 has elements like 3 and 4 that are not in s2,
# so the result is False.
print(s1.issubset(s2))

# Output:
# False


# 🔎 Check if s1 is a superset of s2
# issuperset() checks whether s1 contains
# every element of s2.
#
# s1 does not contain all the elements of s2,
# so the result is False.
print(s1.issuperset(s2))

# Output:
# False


# 🚫 Check if two sets are disjoint
# isdisjoint() checks whether the two sets have
# NO common elements.
#
# Since s1 and s2 have 1, 2 and 90 in common,
# they are not disjoint.
print(s1.isdisjoint(s2))

# Output:
# False
