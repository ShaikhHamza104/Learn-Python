"""
📚 Topic: Chapter 05 Exercise - Problem 4

Determine the length of a set after adding `20`, `20.0`, and `'20'`.

💡 Key points:
    1️⃣ Value equality between `20 == 20.0` evaluates to True
    2️⃣ Identical hash values mean float `20.0` collides with int `20`
    3️⃣ Final set length is 2: containing `20` (or `20.0`) and string `'20'`
"""
# 🧺 Create an empty set
s = set()


# ➕ Add an integer
s.add(20)


# ➕ Add a float
# 20.0 is considered equal to 20 in Python,
# so the set will not store it as a separate value.
s.add(20.0)


# ➕ Add a string
# "20" is different from the number 20,
# so it will be stored separately.
s.add("20")


# 📏 Find the number of unique values in the set
print(len(s))

# Output:
# 2
