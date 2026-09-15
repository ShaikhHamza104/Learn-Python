"""
📚 Topic: Chapter 05 Exercise - Problem 8

Demonstrate what happens when multiple friends share the same favorite
language (duplicate values).

💡 Key points:
    1️⃣ Values in dictionaries do not need to be unique
    2️⃣ Multiple distinct keys can map to identical values
    3️⃣ Both entries persist without interference
"""
# 📚 Create a dictionary containing friends and their
# favorite programming languages.
languages = {
    "Rahul": "Php",
    "Harry": "Python",
    # ✅ "Python" is already used as a value by Harry,
    # but duplicate values are allowed in a dictionary.
    "Hamza": "Python",
}

# ⚠️ A repeated key replaces its earlier value.
languages["Rahul"] = "Django"


# 📋 Display the final dictionary
print(languages)

# Output:
# {'Rahul': 'Django', 'Harry': 'Python', 'Hamza': 'Python'}


# 💡 Remember:
#
# Dictionary keys  → Must be unique ❌ duplicate keys are not allowed
# Dictionary values → Can be repeated ✅ duplicate values are allowed
#
# Example:
#
# "Harry": "Python"
# "Hamza": "Python"
#
# This is completely valid because "Harry" and "Hamza"
# are two different keys.
