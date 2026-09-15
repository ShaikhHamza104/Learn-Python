"""
📚 Topic: Chapter 07 Exercise - Problem 8

Print a right-angled triangle star pattern using nested loops.

💡 Key points:
    1️⃣ Outer loop controlling rows
    2️⃣ Inner loop controlling column star output
    3️⃣ Using `end=""` to control newline output
"""
# 🔢 Define the number of rows
n = 3

# 🔄 Outer loop controls the rows
for i in range(1, n + 1):
    # ⭐ Inner loop prints '*' i times
    for j in range(i):
        print("*", end="")

    # ↩️ Move to the next line after printing the stars
    print()
