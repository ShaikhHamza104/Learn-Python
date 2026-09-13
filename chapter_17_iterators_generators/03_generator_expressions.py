"""
📚 Topic: Generator Expressions

This script demonstrates generator expressions - the memory-efficient
cousin of list comprehensions - and shows exactly how much memory they
save.

💡 Key points:
    1️⃣ the basic syntax for a generator expression using ()
    2️⃣ how sys.getsizeof fits into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    generator expressions affects the result.
"""

import sys

# ---------------------------------------------------
# List comprehension (builds the WHOLE list in memory right away)
# ---------------------------------------------------
L = [i**2 for i in range(1, 101)]

for value in L:
    print(value)


# ---------------------------------------------------
# Generator expression (looks almost identical, () instead of [])
# ---------------------------------------------------
# This does NOT calculate anything yet - it only creates a generator
# object that will calculate each value one at a time, only when asked.
gen = (i**2 for i in range(1, 101))

for value in gen:
    print(value)


# ---------------------------------------------------
# Proving the memory difference
# ---------------------------------------------------
L = [x for x in range(100000)]
gen = (x for x in range(100000))

print("Size of L in memory:", sys.getsizeof(L))
print("Size of gen in memory:", sys.getsizeof(gen))
# L takes up real memory for every single number
# gen takes up almost nothing - it only remembers HOW to make each number


# ---------------------------------------------------
# 🆚 List comprehension vs Generator expression
# ---------------------------------------------------
# [i for i in range(10)]     -> list comprehension: builds full list now
# (i for i in range(10))     -> generator expression: builds values lazily
#
# Use a list comprehension when you need to:
#   - use the data more than once
#   - use list-only methods like .append(), .sort(), indexing [i]
#
# Use a generator expression when you:
#   - only need to loop through the data ONCE
#   - are working with a huge (or infinite) amount of data


# ---------------------------------------------------
# A generator expression passed straight into a function
# ---------------------------------------------------
# You don't even need extra parentheses when it's the only argument
total = sum(i**2 for i in range(1, 11))
print("Sum of squares 1-10:", total)


# ---------------------------------------------------
# 💡 Why this matters for Data Science
# ---------------------------------------------------
# When processing a huge CSV or a folder of thousands of images, a
# generator expression lets you calculate stats (sum, average, max)
# on the fly without ever loading everything into memory at once.
