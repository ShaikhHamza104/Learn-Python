"""
📚 Topic: Chapter 07 Exercise - Problem 10

Print the multiplication table of a given number in reverse order (10 to 1).

💡 Key points:
    1️⃣ Using negative step in `range(10, 0, -1)`
    2️⃣ Iterating backwards through multipliers
    3️⃣ Displaying formatted multiplication output
"""
# 🔢 Take a number from the user
num = int(input("Enter a number: "))

# 🔄 Loop from 10 down to 1
for i in range(10, 0, -1):
    # ✖️ Print the multiplication result
    print(f"{num} x {i} = {num * i}")
