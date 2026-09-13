"""
📚 Topic: Mod2 Module Use

This script demonstrates mod2 module use using user input and imports.

💡 Key points:
    1️⃣ the basic syntax for mod2 module use
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    mod2 module use affects the result.
"""

import mod1_intro_module

a = int(input("Enter number "))
b = int(input("Enter number "))
c = mod1_intro_module.Calculator(a, b)
print(c.add(a, b))
print(c.sub(a, b))
print(c.mul(a, b))
print(c.div(a, b))
