"""
📚 Topic: Chapter 06 Exercise - Problem 6

Calculate student letter grades based on percentage ranges (Ex, A, B, C, D, F).

💡 Key points:
    1️⃣ Validating input bounds (0 to 100)
    2️⃣ Categorizing numerical scores into discrete grade buckets
    3️⃣ Using an ordered `if-elif-else` ladder
"""
# 📝 Take marks from the user
marks = int(input("Enter your marks: "))

# 🚨 Check whether the marks are valid
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")

# 🏆 90 - 100 → Ex
elif marks >= 90:
    print("Ex")

# 🅰️ 80 - 89 → A
elif marks >= 80:
    print("A")

# 🅱️ 70 - 79 → B
elif marks >= 70:
    print("B")

# 🅲️ 60 - 69 → C
elif marks >= 60:
    print("C")

# 🅳️ 50 - 59 → D
elif marks >= 50:
    print("D")

# ❌ Below 50 → F
else:
    print("F")
