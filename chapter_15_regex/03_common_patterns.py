"""
📚 Topic: Common Regex Patterns

This script demonstrates real-world regex patterns for validating
emails, phone numbers, and dates.

💡 Key points:
    1️⃣ the basic syntax for common validation patterns
    2️⃣ how re.fullmatch fits into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    common regex patterns affects the result.
"""

import re

# ---------------------------------------------------
# email validation
# ---------------------------------------------------
email_pattern = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"

emails = ["hamza@gmail.com", "not-an-email", "test.user@vsit.edu.in"]

for email in emails:
    # fullmatch() checks that the ENTIRE string matches, start to end
    if re.fullmatch(email_pattern, email):
        print(f"{email} -> ✅ valid")
    else:
        print(f"{email} -> ❌ invalid")

# ---------------------------------------------------
# phone number validation (basic 10-digit Indian style)
# ---------------------------------------------------
phone_pattern = r"^[6-9]\d{9}$"

phones = ["9876543210", "12345", "8123456789"]

for phone in phones:
    if re.fullmatch(phone_pattern, phone):
        print(f"{phone} -> ✅ valid phone number")
    else:
        print(f"{phone} -> ❌ invalid phone number")

# ---------------------------------------------------
# date validation (dd-mm-yyyy format)
# ---------------------------------------------------
date_pattern = r"^\d{2}-\d{2}-\d{4}$"

dates = ["09-09-2026", "2026-09-09", "9-9-2026"]

for date in dates:
    if re.fullmatch(date_pattern, date):
        print(f"{date} -> ✅ valid date format")
    else:
        print(f"{date} -> ❌ invalid date format")

# ---------------------------------------------------
# extracting all emails found inside a block of text
# ---------------------------------------------------
message = """
Contact us at support@vsit.edu.in or hamza.shaikh@gmail.com
for more information.
"""

found_emails = re.findall(
    email_pattern.replace("^", "").replace("$", ""),
    message
)

print(found_emails)

# ---------------------------------------------------
# 💡 Why this matters for Data Science
# ---------------------------------------------------
# Real datasets are messy - regex is one of the fastest ways to clean,
# validate, or extract structured info (emails, dates, IDs) from raw
# text before it ever reaches pandas.
