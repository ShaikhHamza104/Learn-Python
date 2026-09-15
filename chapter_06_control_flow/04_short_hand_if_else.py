"""
📚 Topic: Ternary Operator (Conditional Expressions)

This script demonstrates Python's conditional expression syntax (ternary
operator) for evaluating single-line inline decisions.

💡 Key points:
    1️⃣ Syntax: `value_if_true if condition else value_if_false`
    2️⃣ Evaluating expressions inline for concise variable assignment
    3️⃣ Maintaining readability: avoid deeply nesting ternary operators

🧠 Beginner tip:
    Use ternary expressions for simple assignments; for multi-step logic,
    use standard multi-line `if-else` statements.
"""
# 🔢 Take the first number from the user
a = int(input("Enter number: "))

# 🔢 Take the second number from the user
b = int(input("Enter number: "))

# 🔍 Print the greater number
print(a) if a > b else print(b)
