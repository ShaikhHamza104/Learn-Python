"""
📚 Topic: Tuple Operations

This script demonstrates operations available on tuples, such as indexing,
slicing, concatenation, and membership tests.

💡 Key points:
    1️⃣ Accessing elements by positive and negative indices
    2️⃣ Joining tuples with `+` and repeating with `*`
    3️⃣ Tuple unpacking into individual variables

🧠 Beginner tip:
    Because tuples are immutable, operations like `+` produce a new tuple
    rather than modifying an existing one.
"""
# 📦 Creating a tuple
# A tuple allows us to store multiple values inside a single variable.
# Tuples keep the values in the same order in which we add them.
#
# 💡 Once this tuple is created, we cannot change its existing elements.
t = (1, 2, 3, 4, 5, 6)


# 🔗 Concatenating (joining) two tuples
# We can join two tuples together using the + operator.
t1 = (7, 8, 9, 10)

# Here, Python joins t and t1 and creates a new tuple.
# The original tuples remain unchanged.
t3 = t + t1

print(t3)

# Output:
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# 🔁 Repeating a tuple
# The * operator allows us to repeat the elements of a tuple.
#
# Here, t is repeated 3 times.
# Python creates a new tuple containing all three repetitions.
t4 = t * 3

print(t4)

# Output:
# (1, 2, 3, 4, 5, 6,
#  1, 2, 3, 4, 5, 6,
#  1, 2, 3, 4, 5, 6)
