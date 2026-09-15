"""
📚 Topic: Exercise 3 - Input Type Verification

This exercise prompts the user for terminal input, displays the value, and
uses `type()` to verify that raw user input always defaults to `<class 'str'>`.

💡 Key points:
    1️⃣ Prompting user input with `input()`
    2️⃣ Inspecting the resulting runtime data type with `type()`
    3️⃣ Confirming that all captured console input is initially a string

🧠 Beginner tip:
    Even if the user types digits like `42`, `type(input())` will report
    `<class 'str'>` until explicitly cast with `int()` or `float()`.
"""

name = input("Enter your name ")
print("Your name is ", name)
print(type(name))  # <class 'str'>
