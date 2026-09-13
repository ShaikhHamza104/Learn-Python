"""
📚 Topic: Dict

This script demonstrates dict using basic Python syntax.

💡 Key points:
    1️⃣ the basic syntax for dict
    2️⃣ how basic Python syntax fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    dict affects the result.
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
