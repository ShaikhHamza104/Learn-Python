"""
📚 Topic: Object Introspection with dir()

This script demonstrates using `dir()` to inspect attributes and callable
methods exposed by built-in Python types.

💡 Key points:
    1️⃣ Introspecting built-in data types like `list`, `tuple`, and `str`
    2️⃣ Distinguishing dunder (`__...__`) methods from public API methods
    3️⃣ Exploring available functionality during debugging

🧠 Beginner tip:
    Combine `dir(obj)` with `help(obj.method)` in the interactive REPL to
    discover how methods work without leaving the terminal.
"""
# 📦 Creating a list
# This list contains six numbers.
li = [1, 2, 3, 4, 5, 0]


# 🔍 Exploring everything available for this list
# dir() returns a list of attributes and methods that can be used with `l`.
#
# This is especially helpful when you want to discover what operations
# Python provides for a particular object.
print(dir(li))
