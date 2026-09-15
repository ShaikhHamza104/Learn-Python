"""
📚 Topic: The `for...else` Construct

This script demonstrates Python's unique `else` clause attached to loops,
which executes only when the loop completes without being broken.

💡 Key points:
    1️⃣ The `else` block runs after the loop finishes all iterations normally
    2️⃣ If the loop terminates early via `break`, the `else` block is skipped
    3️⃣ Ideal for search algorithms where an item is not found

🧠 Beginner tip:
    Think of `loop...else` as "no-break": it runs only if no `break` occurred
    during loop execution.
"""
# 📋 Create a list of numbers
l = [1, 2, 3, 4, 5, 6]  # noqa: E741

# 🔄 Loop through each element in the list
for i in l:
    print(i)

# ✅ This runs after the for loop finishes normally
print("Done")
