"""
📚 Topic: Common String Methods

This script demonstrates essential built-in string methods for measuring
length, case transformation, substring searching, and character verification.

💡 Key points:
    1️⃣ Querying properties: `len()`, `.startswith()`, `.endswith()`
    2️⃣ Case modification: `.upper()`, `.lower()`, `.capitalize()`
    3️⃣ Substring search & inspection: `.find()`, `.count()`, `.isalnum()`

🧠 Beginner tip:
    Because strings are immutable, methods like `.upper()` or `.replace()`
    do not change the original string; they return a brand-new string copy.
"""

name = "hamza"
# string are immutable
# To find the length of string
print(len(name))

# To find the start of the string
print(name.startswith("Ha"))

# To find the end of the string
print(name.endswith("za"))

# to convert string of all character in upper case
print(name.upper())

# to convert string of all character in lower case
print(name.lower())

# to convert first character in upper case latter
print(name.capitalize())

# to find the first occurrence letter
print(name.find("a", 0))

# Check if all characters in the string are alphanumeric (letters and numbers)
print(name.isalnum())

# to find the number of occurrences
print(name.count("a"))

# to find the index of character at first occurrence
print(name.index("z"))

# check that the string contains alphabetic characters
print(name.isalpha())

# check that the string contains digits
print(name.isdigit())

# to replace character
print(name.replace("h", "H"))

s = "         Python                       "
# Remove leading and trailing whitespaces from the string
print(s.strip())

s = "Python programming language"
#  splits the string "s" into a list of words
print(s.split())

# Make the first letter in each word upper case:
print(s.title())  # Python Programming Language
