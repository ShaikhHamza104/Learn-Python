"""
📚 Topic: Set Comprehensions

This script demonstrates declarative set comprehensions to build deduplicated
sets with transformed or filtered values.

💡 Key points:
    1️⃣ Syntax: `{expression for item in iterable}`
    2️⃣ Automatic deduplication during comprehension construction
    3️⃣ Conditional inclusion using trailing `if` clauses

🧠 Beginner tip:
    Set comprehensions look like dictionary comprehensions but lack the
    `key: value` colon syntax.
"""
# 🔢 Generate 10 elements in a set using set comprehension
# range(1, 11) generates numbers from 1 to 10.
#
# The set comprehension takes each number and stores it in the set.
s = set(i for i in range(1, 11))

print(s)

# Output:
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# 🟢 Generate even numbers from 10 to 40
# range(10, 41) generates numbers from 10 to 40.
#
# `i % 2 == 0` checks whether a number is even.
# If the remainder is 0 after dividing by 2, the number is even.
s = {i for i in range(10, 41) if i % 2 == 0}

print(s)

# Output:
# {10, 12, 14, 16, 18, 20, 22, 24, 26, 28,
#  30, 32, 34, 36, 38, 40}


# 🟠 Generate odd numbers from 10 to 40
# range(10, 41) generates numbers from 10 to 40.
#
# `i % 2 != 0` checks whether a number is odd.
# If the remainder is NOT 0 after dividing by 2, the number is odd.
#
# ⚠️ The original code used `i % 2 == 0` here,
# which would generate even numbers.
s = {i for i in range(10, 41) if i % 2 != 0}

print(s)

# Output:
# {11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
#  31, 33, 35, 37, 39}
