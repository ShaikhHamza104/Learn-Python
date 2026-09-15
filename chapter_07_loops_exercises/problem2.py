"""
📚 Topic: Chapter 07 Exercise - Problem 2

Greet individuals in a name list whose names start with the letter 'S'.

💡 Key points:
    1️⃣ Iterating through a list of names
    2️⃣ Checking prefix matching with `.startswith()`
    3️⃣ Printing personalized greetings conditionally
"""
# 📋 Store names in a list
names = ["Harry", "Soham", "Sachin", "Rahul"]

# 🔄 Check each name in the list
for name in names:
    # 🔍 Check if the name starts with the letter "S"
    if name.startswith("S"):
        # 👋 Greet the person
        print("Greeting " + name)
