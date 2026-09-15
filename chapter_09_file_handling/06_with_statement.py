"""
📚 Topic: Context Managers & the `with` Statement

This script demonstrates Python's `with` statement for automated and
exception-safe file resource management.

💡 Key points:
    1️⃣ Syntax: `with open(...) as f:`
    2️⃣ Automatic file closure even if exceptions occur inside the block
    3️⃣ Eliminates manual `f.close()` calls

🧠 Beginner tip:
    The `with` statement is the Pythonic standard for file handling. Always
    prefer it over manual `open()` and `close()`.
"""
with open('sample.txt') as f:
    print(f.read())
