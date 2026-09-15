"""
📚 Topic: The `while` Loop

This script demonstrates condition-controlled iteration using `while` loops.

💡 Key points:
    1️⃣ Iterating as long as a condition evaluates to True
    2️⃣ Initializing loop control variables before the loop begins
    3️⃣ Incrementing or updating control variables to avoid infinite loops

🧠 Beginner tip:
    Ensure your loop has a clear exit condition that is eventually reached;
    otherwise, the program will hang in an infinite loop.
"""
# 🔢 Start the counter at 1
i = 1

# 🔄 Keep running while i is less than 6
while i < 6:
    # 🖨️ Print the current value of i
    print(i)

    # ➕ Increase i by 1
    i += 1
