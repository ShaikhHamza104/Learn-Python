"""
📚 Topic: Introduction to Regex (re module)

This script demonstrates the basics of pattern matching in Python using
the built-in re module.

💡 Key points:
    1️⃣ the basic syntax for re.match, re.search and re.findall
    2️⃣ how import re fits into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    introduction to regex affects the result.
"""

# importing re module : re module is a build in module used for
# working with regular expressions (patterns inside text)
import re

text = "Hamza is learning Python in 2026"

# re.match() : checks for a match only at the BEGINNING of the string
result = re.match(r"Hamza", text)
print(result)          # <re.Match object...> if found, else None

# re.search() : checks for a match ANYWHERE in the string
# (stops after finding the first match)
result = re.search(r"Python", text)
print(result)

# re.findall() : returns ALL matches as a list
numbers = re.findall(r"\d+", text)
print(numbers)          # ['2026']

# .group() : gives you the actual matched text (not the Match object)
match = re.search(r"learning \w+", text)
if match:
    print(match.group())    # "learning Python"

# checking IF something matched, using a simple if condition
if re.search(r"Python", text):
    print("Python word found in text!")
else:
    print("Python word not found")
