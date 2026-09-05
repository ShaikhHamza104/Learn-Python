"""
📚 Topic: Opration Dict

This script demonstrates opration dict using basic Python syntax.

💡 Key points:
    1️⃣ the basic syntax for opration dict
    2️⃣ how basic Python syntax fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    opration dict affects the result.
"""


# 📚 Creating a dictionary
# Here, student names are used as keys
# and their marks are stored as values.
mark = {"Rohan": 70, "Harry": 100, "Sonali": 80, "Mari": 75, "Yusuf": 95}


# 🔍 Accessing a value from the dictionary
# We use the key "Rohan" to get Rohan's marks.
print(mark["Rohan"])

# Output:
# 70


# ➕ Adding a new key-value pair
# Here, we add a new student named "Osama"
# and store his marks as 60.
#
# If the key does not already exist, Python adds it to the dictionary.
mark["Osama"] = 60

print(mark)

# Output:
# {'Rohan': 70, 'Harry': 100, 'Sonali': 80,
#  'Mari': 75, 'Yusuf': 95, 'Osama': 60}


# 🗑️ Deleting a key-value pair
# The del statement removes the specified key
# and its corresponding value from the dictionary.
#
# Here, we remove "Mari" and her marks.
del mark["Mari"]

print(mark)

# Output:
# {'Rohan': 70, 'Harry': 100, 'Sonali': 80,
#  'Yusuf': 95, 'Osama': 60}
