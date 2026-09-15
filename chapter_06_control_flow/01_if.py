"""
📚 Topic: The `if` Statement

This script introduces conditional execution in Python using the `if` keyword
to run code blocks only when a condition evaluates to True.

💡 Key points:
    1️⃣ Boolean condition evaluation (True or False)
    2️⃣ Python indentation defines the block of code inside the `if`
    3️⃣ If the condition is False, the indented block is skipped entirely

🧠 Beginner tip:
    In Python, indentation (typically 4 spaces) is syntactically mandatory,
    replacing curly braces `{}` used in other languages.
"""
# 👤 Ask the user to enter their age
age = int(input("Enter your age: "))

# 🔍 Check if the age is less than 18
if age < 18:
    print("You cannot vote")
