r"""
📚 Topic: Escape Sequences in Python Strings

This script demonstrates using escape characters (`\`, `\n`, `\t`) and
quote mixing to include reserved characters inside string literals.

💡 Key points:
    1️⃣ Nesting different quote styles (single inside double and vice versa)
    2️⃣ Using `\n` to insert newline line-breaks into strings
    3️⃣ Escaping matching quotes using the backslash escape character `\`

🧠 Beginner tip:
    If your string contains many backslashes (such as regexes or file paths),
    prefix it with `r` to make it a raw string: `r"C:\Users\name"`.
"""

string = "He said,'I am good'"
print(string)  # He said,'I am good'

string = 'I am learning "python"'
print(string)  # I am learning "python"
string = "I am Hamza.\nI am learning 'python programming' language"
# I am Hamza.
# I am learning 'python programming' language
print(string)
