"""
📚 Topic: Chapter 06 Exercise - Problem 5

Determine whether a given name is present in an authorized list of names.

💡 Key points:
    1️⃣ Storing allowed names in a list
    2️⃣ Normalizing user input casing using `.capitalize()`
    3️⃣ Checking membership using the `in` operator
"""
# 📋 Create a list of names
list_of_name = ["Rohit", "Rajo", "Harry", "Hamza"]

# 👤 Ask the user for their name
# 🔤 capitalize() makes the first letter uppercase
name = input("Enter your name: ").capitalize()

# 🔍 Check whether the name exists in the list
if name in list_of_name:
    print("Your name is in the list ✅")

# ❌ Name is not present in the list
else:
    print("Your name is not in the list ❌")
