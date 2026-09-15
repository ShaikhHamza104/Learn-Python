"""
📚 Topic: Importing and Using Module Members

This script demonstrates different import styles, including importing entire
modules and aliasing module names.

💡 Key points:
    1️⃣ Standard import: `import module`
    2️⃣ Aliasing with `as`: `import module as alias`
    3️⃣ Accessing exported module attributes and functions

🧠 Beginner tip:
    Use descriptive aliases to keep code concise without sacrificing
    readability.
"""


import mod1_intro_module

a = int(input("Enter number "))
b = int(input("Enter number "))
c = mod1_intro_module.Calculator(a, b)
print(c.add(a, b))
print(c.sub(a, b))
print(c.mul(a, b))
print(c.div(a, b))
