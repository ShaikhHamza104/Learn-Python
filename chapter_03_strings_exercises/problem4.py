"""
📚 Topic: Exercise 4 - Whitespace Sanitization with `.replace()`

This exercise sanitizes irregular spacing in text by replacing double
spaces (`"  "`) with single spaces (`" "`) using `str.replace()`.

💡 Key points:
    1️⃣ Identifying unwanted whitespace patterns in text
    2️⃣ Cleaning text by substituting double spaces with single spaces
    3️⃣ Producing normalized, sanitized string copies

🧠 Beginner tip:
    For complex whitespace with multiple irregular spaces or tabs,
    `" ".join(text.split())` is a powerful idiom that normalizes all spaces.
"""

string = "Python is programming language.Its easy  to understand language"
print(string.replace("  ", " "))
