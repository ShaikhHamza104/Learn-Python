"""
📚 Topic: M02 Module Use

This script demonstrates m02 module use using user input and imports.

💡 Key points:
    1️⃣ the basic syntax for m02 module use
    2️⃣ how user input fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    m02 module use affects the result.
"""

import m01_intro_module

a = int(input("Enter number "))
b = int(input("Enter number "))
c = m01_intro_module.Calculator(a, b)
print(c.add(a, b))
print(c.sub(a, b))
print(c.mul(a, b))
print(c.div(a, b))
