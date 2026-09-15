"""
📚 Topic: Instance vs Class Attributes

This script demonstrates the difference between class attributes (shared by
all instances) and instance attributes (unique to each instance).

💡 Key points:
    1️⃣ Class attributes are defined directly in the class body
    2️⃣ Instance attributes attach to individual objects (`obj.attr = val`)
    3️⃣ Instance attributes take precedence over class attributes upon lookup

🧠 Beginner tip:
    Python looks for an attribute on the instance first; if not found, it
    falls back to searching the class definition.
"""


class Employee:
    salary = 10000  # This is class attribute
    company = "Microsoft"
    language = "Python"


emp1 = Employee()
emp2 = Employee()

emp1.name = "Hamza"  # This is an object/ instance attribute
print(emp1.name, emp1.company, emp1.language)

emp2.language = "Java"
print(emp2.language, emp2.company)
