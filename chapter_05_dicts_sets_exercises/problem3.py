"""
📚 Topic: Chapter 05 Exercise - Problem 3

Verify whether a set can simultaneously hold integer `18` and string `'18'`.

💡 Key points:
    1️⃣ Distinguishing integer vs string types in Python
    2️⃣ Hash equality and type sensitivity in sets
    3️⃣ Both elements coexist because their types and hashes differ
"""
# 🧺 Create a set containing an integer and a string
# 18 is an integer, while "18" is a string.
s = set({18, "18"})


# 📋 Print the set and its data type
print(s, type(s))

# Output:
# {18, '18'} <class 'set'>

# 💡 Notice:
# The set contains both values because Python treats
# the integer 18 and the string "18" as different values.
