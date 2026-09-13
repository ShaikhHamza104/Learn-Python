"""
📚 Topic: Opration Tuple

This script demonstrates opration tuple using basic Python syntax.

💡 Key points:
    1️⃣ the basic syntax for opration tuple
    2️⃣ how basic Python syntax fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    opration tuple affects the result.
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
