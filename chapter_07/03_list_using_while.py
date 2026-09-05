"""
📚 Topic: List Using While

This script demonstrates list using while using while loops.

💡 Key points:
    1️⃣ the basic syntax for list using while
    2️⃣ how while loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    list using while affects the result.
"""

# 📋 Create a list of names
l = ["Harry", "Rohan", "Ramesh", "Rahul", "Riya"]  # noqa: E741

# 🔢 Start the index from 0
i = 0

# 🔄 Run the loop while i is a valid list index
while i < len(l):
    # 🖨️ Print the element at the current index
    print(l[i])

    # ➡️ Move to the next index
    i += 1
