"""
📚 Topic: Groups and Substitution in Regex

This script demonstrates how to capture parts of a match using groups,
and how to replace text using re.sub.

💡 Key points:
    1️⃣ the basic syntax for capturing groups with ()
    2️⃣ how re.sub fits into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    groups and substitution affects the result.
"""

import re

# ---------------------------------------------------
# groups : parts of the pattern wrapped in () can be pulled out separately
# ---------------------------------------------------
date_text = "Today's date is 09-09-2026"

match = re.search(r"(\d{2})-(\d{2})-(\d{4})", date_text)

if match:
    print(match.group())     # full match: 09-09-2026
    print(match.group(1))    # day: 09
    print(match.group(2))    # month: 09
    print(match.group(3))    # year: 2026
    # print(match.group(4))    # Error: No group 4

# ---------------------------------------------------
# named groups : giving each group a readable name instead of a number
# ---------------------------------------------------
pattern = r"(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})"
match = re.search(pattern, date_text)

if match:
    print(match.group("day"))
    print(match.group("month"))
    print(match.group("year"))

# ---------------------------------------------------
# re.sub() : find a pattern and replace it with something else
# ---------------------------------------------------
sentence = "My phone number is 9876543210"

# replacing every digit with an asterisk (like hiding sensitive data)
hidden = re.sub(r"\d", "*", sentence)
print(hidden)

# ---------------------------------------------------
# re.sub() using groups : reusing part of the match in the replacement
# ---------------------------------------------------
messy_date = "2026-09-09"

# converting yyyy/mm/dd -> dd-mm-yyyy using group numbers \1 \2 \3
fixed_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3-\2-\1", messy_date)
print(fixed_date)     # 09-09-2026

# ---------------------------------------------------
# re.split() : splitting a string using a pattern instead of a fixed string
# ---------------------------------------------------
data = "Hamza, Ali;  Sara, Zoya"
names = re.split(r"[,;]\s*", data)
print(names)   # ['Hamza', 'Ali', 'Sara', 'Zoya']
