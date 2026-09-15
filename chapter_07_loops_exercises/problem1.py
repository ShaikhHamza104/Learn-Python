"""
📚 Topic: Chapter 07 Exercise - Problem 1

Print the multiplication table of a user-specified number using a `for` loop.

💡 Key points:
    1️⃣ Prompting user for an integer
    2️⃣ Iterating from 1 to 10 with `range(1, 11)`
    3️⃣ Formatting the multiplication table output with f-strings
"""
# 🔢 Take a number from the user
num = int(input("Enter a number: "))

# 🔄 Loop from 1 to 10
for i in range(1, 11):
    # ✖️ Multiply the given number by i
    # f-string makes the output easy to read
    print(f"{num} x {i} = {num * i}")
