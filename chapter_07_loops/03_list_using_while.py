"""
📚 Topic: Traversing Sequences with a `while` Loop

This script demonstrates iterating through lists using index-based `while`
loops.

💡 Key points:
    1️⃣ Using an integer index counter starting at 0
    2️⃣ Guarding the loop with `index < len(list)`
    3️⃣ Accessing elements by index and incrementing the counter

🧠 Beginner tip:
    While `while` loops work for sequence traversal, Python's
    `for item in list` is preferred and idiomatic.
"""
# 📋 Create a list of names
names = ["Harry", "Rohan", "Ramesh", "Rahul", "Riya"]

# 🔢 Start the index from 0
i = 0

# 🔄 Run the loop while i is a valid list index
while i < len(names):
    # 🖨️ Print the element at the current index
    print(names[i])

    # ➡️ Move to the next index
    i += 1
