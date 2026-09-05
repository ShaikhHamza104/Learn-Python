"""
📚 Topic: Set Method

This script demonstrates set method using basic Python syntax.

💡 Key points:
    1️⃣ the basic syntax for set method
    2️⃣ how basic Python syntax fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    set method affects the result.
"""


# 📦 Creating a set
s = {1, 2, 10, 18, 17, 90}


# ➕ Add one element to the set
# add() is used when we want to add a single value.
s.add(100)

print(s)


# ➕➕ Add multiple elements to the set
# update() allows us to add multiple values at once.
#
# Here, 3, 4 and 5 are added to the existing set.
s.update({3, 4, 5})

print(s)


# 🗑️ Remove one element from the set
# remove() deletes the specified element.
#
# Here, the value 1 is removed from the set.
s.remove(1)

print(s)


# 🛡️ Remove an element safely
# discard() also removes an element from the set.
#
# The value "100" is a string, while the set contains
# the number 100.
#
# Since the string "100" is NOT present, nothing is removed.
# Unlike remove(), discard() does not give an error.
s.discard("100")

print(s)


# 🎲 Remove a random/arbitrary element
# pop() removes and returns an arbitrary element from the set.
#
# Because sets are unordered, we should not expect a specific
# element to be removed every time.
s.pop()

print(s)


# 📋 Copy the set into another set
# copy() creates a new set containing the same elements.
#
# Now `s1` is a separate copy of `s`.
s1 = s.copy()

print(s1)


# 🧹 Clear all elements from s1
# clear() removes every element from the set.
s1.clear()

print(s1)

# Output:
# set()

# 💡 Beginner tip:
# `clear()` makes the set empty, but the set itself still exists.
