"""
📚 Topic: Exercise 3 - Double Space Detection with `.find()`

This exercise inspects a string for irregular double spacing using the
`.find()` method, checking whether a substring occurs in the text.

💡 Key points:
    1️⃣ Searching for substrings using `str.find("  ")`
    2️⃣ Checking the index return value against `-1` (not found)
    3️⃣ Avoiding truthiness pitfalls with index `0`

🧠 Beginner tip:
    `.find()` returns `-1` when a substring is missing. Never test
    `if s.find("..."):` directly, because index `0` is falsy in Python!
"""

string = "Python is programming language.Its easy to understand language  "
if string.find("  ") != -1:
    print("Double space detected")
