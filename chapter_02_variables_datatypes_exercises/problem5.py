"""
📚 Topic: Exercise 5 - Calculating Average with Precedence

This exercise prompts the user for two numbers and calculates their arithmetic
mean, demonstrating correct operator precedence using parentheses.

💡 Key points:
    1️⃣ Converting terminal inputs to floating-point numbers
    2️⃣ Grouping the sum inside parentheses `(a + b)` before dividing
    3️⃣ Displaying the resulting calculated average

🧠 Beginner tip:
    Without parentheses, `a + b / 2` divides `b` first due to standard
    order of operations (PEMDAS). Always group numerators in formulas!
"""

num1 = int(input("Enter first number"))
num2 = int(input("Enter second  number"))
avg = (num1 + num2) / 2
print("The average of two numbers is", avg)
