"""
📚 Topic: Runtime Type Inspection with `type()`

This script demonstrates using Python's built-in `type()` function to inspect
the underlying class of any variable or object during execution.

💡 Key points:
    1️⃣ Passing variables or literal values to `type()`
    2️⃣ Inspecting the resulting `<class '...'>` representation
    3️⃣ Verifying dynamic type classifications across diverse literals

🧠 Beginner tip:
    For production validation, prefer `isinstance(var, int)` over
    `type(var) == int` because `isinstance` respects class inheritance.
"""

a = 10
print(type(a))  # <class 'int'>

b = 20.3
print(type(b))  # <class 'float'>

c = "Python"
print(type(c))  # <class 'str'>

d = None
print(type(d))  # <class 'NoneType'>

e = True
print(type(e))  # <class 'bool'>
