"""
📚 Topic: Tuple Method

This script demonstrates tuple method using basic Python syntax.

💡 Key points:
    1️⃣ the basic syntax for tuple method
    2️⃣ how basic Python syntax fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    tuple method affects the result.
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
