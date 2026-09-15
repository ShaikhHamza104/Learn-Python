"""
📚 Topic: Explicit Type Casting & Conversion

This script demonstrates explicit type conversion using Python constructor
functions (`int()`, `float()`, `str()`), transforming data between incompatible
class representations safely.

💡 Key points:
    1️⃣ Converting numeric strings to integers with `int("10")`
    2️⃣ Truncating floating-point numbers to integers (dropping decimals)
    3️⃣ Casting boolean values to integers (`True` -> `1`, `False` -> `0`)

🧠 Beginner tip:
    Calling `int()` on a float truncates toward zero—it does not round to
    the nearest integer. Use `round()` if mathematical rounding is needed.
"""

n = "10"

f = int(n)

print(type(f))  # <class 'int'>

n = 28.99

print(int(n))  # 28

d = True
print(type(d))  # <class 'bool'>

print(int(d))  # 1
