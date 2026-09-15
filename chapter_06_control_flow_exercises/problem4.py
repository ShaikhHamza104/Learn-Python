"""
📚 Topic: Chapter 06 Exercise - Problem 4

Check whether a given username contains fewer than 10 characters.

💡 Key points:
    1️⃣ Measuring string length using `len()`
    2️⃣ Comparing character count against threshold with `<`
    3️⃣ Providing validation feedback
"""
# 👤 Ask the user to enter their username
username = input("Enter your username: ")

# 🔢 Check whether the username has less than 10 characters
if len(username) < 10:
    print("Username contains less than 10 characters")
