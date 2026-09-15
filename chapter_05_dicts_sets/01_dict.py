"""
📚 Topic: Python Dictionaries

This script introduces dictionaries as mutable, key-value mapping structures
providing constant-time O(1) average lookup performance.

💡 Key points:
    1️⃣ Defining dictionaries using curly braces `{}` and `key: value` pairs
    2️⃣ Accessing values using their unique keys
    3️⃣ Key immutability requirement: keys must be hashable types

🧠 Beginner tip:
    Dictionary keys must be unique. If a duplicate key is assigned, the new
    value overwrites the previous one.
"""
# 📚 Creating a dictionary
# Here, we store the names of students as keys
# and their marks as values.
mark = {"Harry": 100, "Rohan": 80, "Hamza": 75}


# 🔍 Print the complete dictionary
# type() tells us what type of data `mark` is.
print(mark, type(mark))

# Output:
# {'Harry': 100, 'Rohan': 80, 'Hamza': 75} <class 'dict'>


# 🎯 Access Harry's marks
# We use the key "Harry" to get its corresponding value.
print(mark["Harry"])

# Output:
# 100


# 🎯 Access Hamza's marks
# Here, "Hamza" is the key, so Python returns the value 75.
print(mark["Hamza"])

# Output:
# 75
