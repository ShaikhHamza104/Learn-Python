"""
📚 Topic: Tuple Methods

This script explores the two built-in methods supported by immutable tuples:
`count()` and `index()`.

💡 Key points:
    1️⃣ Counting occurrences with `tuple.count(value)`
    2️⃣ Finding the first matching index with `tuple.index(value)`
    3️⃣ Determining tuple length using `len(tuple)`

🧠 Beginner tip:
    Because tuples cannot be mutated, they have far fewer methods than lists,
    making them lightweight and memory-efficient.
"""
# 📦 Creating a tuple
# This tuple contains 10 elements.
# Notice that the value 6 appears three times.
t = (1, 2, 3, 8, 4, 5, 6, 6, 6, 7)


# 📏 Finding the length of the tuple
# len() tells us the total number of elements inside the tuple.
#
# Since t contains 10 elements, the result will be 10.
print(len(t))

# Output:
# 10


# 🔢 Counting how many times a value appears
# count() tells us how many times a particular value occurs in the tuple.
#
# Here, we are checking how many times the number 6 appears.
# There are three 6s in the tuple, so the result is 3.
print(t.count(6))

# Output:
# 3


# 🔎 Finding the position (index) of an element
# index() returns the position of the first occurrence of the value.
#
# Here, the number 7 is at index 9.
# Remember: Python starts counting positions from 0.
print(t.index(7))

# Output:
# 9
