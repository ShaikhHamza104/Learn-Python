"""
📚 Topic: Chapter 07 Exercise - Problem 9

Print a hollow square star pattern of size `n`.

💡 Key points:
    1️⃣ Printing solid border stars for first and last rows
    2️⃣ Printing edge stars with hollow middle spaces for interior rows
    3️⃣ Conditional row formatting
"""
# 🔢 Take the number of rows from the user
n = int(input("Enter a number: "))

# 🔄 Loop through each row
for i in range(1, n + 1):
    # ⭐ First and last rows contain n stars
    if i == 1 or i == n:
        print("* " * n)

    # ⭐ Middle rows contain stars at both ends
    else:
        print("*" + " " * (2 * n - 3) + "*")
