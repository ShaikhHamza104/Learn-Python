"""
📚 Topic: Chapter 05 Exercise - Problem 7

Demonstrate what happens when duplicate keys (friends with same name) are
inserted into a dictionary.

💡 Key points:
    1️⃣ Dictionary keys must remain unique
    2️⃣ Inserting a duplicate key overwrites its existing value
    3️⃣ Only the latest assigned value is preserved
"""
# 📚 Create a dictionary containing friends and their
# favorite programming languages.
languages = {
    "Rahul": "Php",
    "Harry": "Python",
    "Hamza": "Datascience",
}

# ⚠️ A repeated key replaces its earlier value.
languages["Harry"] = "Django"


# 📋 Display the final dictionary
print(languages)

# Output:
# {'Rahul': 'Php', 'Harry': 'Django', 'Hamza': 'Datascience'}


# 💡 Important:
# Dictionary keys must be unique.
#
# If the same key is used again:
#
# "Harry": "Python"
# "Harry": "Django"
#
# Python keeps only:
#
# "Harry": "Django"
#
# The latest value replaces the previous value.
