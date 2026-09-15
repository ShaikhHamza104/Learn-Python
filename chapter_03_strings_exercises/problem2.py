"""
📚 Topic: Exercise 2 - Template Letter Placeholder Replacement

This exercise demonstrates filling placeholders in a multi-line string
template by chaining multiple `.replace()` method calls sequentially.

💡 Key points:
    1️⃣ Defining multi-line template strings with delimiter tags
    2️⃣ Chaining `.replace()` calls to substitute placeholders
    3️⃣ Generating dynamic output without altering the original template

🧠 Beginner tip:
    Each `.replace()` call returns a new string, enabling fluent method
    chaining: `template.replace("<A>", a).replace("<B>", b)`.
"""

letter = """
Dear <|Name|>,
You are selected!
<|Date|>
"""
name = "Hamza"
date = "09-05-2024"
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))
