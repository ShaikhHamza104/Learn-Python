"""
📚 Topic: Iterating with enumerate()

This script demonstrates using Python's built-in `enumerate()` function to
track loop indices and elements cleanly.

💡 Key points:
    1️⃣ Unpacking index and value pairs inside `for` loops
    2️⃣ Setting custom start index offsets using `start=1`
    3️⃣ Eliminating manual index counter variables

🧠 Beginner tip:
    Prefer `enumerate(iterable)` over `range(len(iterable))` for cleaner,
    more Pythonic iteration.
"""
# 📦 Creating a list of numbers
# This list contains six numbers.
li = [1, 2, 3, 4, 5, 6]


# 🔢 Looping through the list with enumerate()
# enumerate() gives us two things on every loop:
#   1️⃣ index   → position of the element
#   2️⃣ element → actual value
#
# Example:
# index = 0, element = 1
# index = 1, element = 2
# and so on...
for index, element in enumerate(li):

    print(index, element)

# Output:
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
# 5 6


# 👥 Creating another list
# Here we have a list of names.
l2 = ["Rohan", "Rahol", "Rohi", "Roshan", "Riha"]


# 🔄 Looping through the names with enumerate()
# Again, enumerate() gives us both the index and the value.
for index, ele in enumerate(l2):

    # 🎯 Check if this is the first element
    # Python starts indexing from 0, so index == 0 means
    # this is the first name in the list.
    if index == 0:

        # 👋 For the first name, print "hi" before the name.
        print("hi", ele)

    else:

        # 📝 For all other names, simply print the name.
        print(ele)

# Output:
# hi Rohan
# Rahol
# Rohi
# Roshan
# Riha
