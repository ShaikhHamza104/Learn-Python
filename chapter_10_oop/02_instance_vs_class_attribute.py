"""
📚 Topic: Instance vs Class Attributes

This script demonstrates instance vs class attributes using for loops and
classes.

💡 Key points:
    1️⃣ the basic syntax for instance vs class attributes
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    instance vs class attributes affects the result.
"""


class Employee:
    salary = 10000  # This is class attribut
    company = "Micosoft"
    language = "Python"


emp1 = Employee()
emp2 = Employee()

emp1.name = "Hamza"  # This is an object/ instance attribut
print(emp1.name, emp1.company, emp1.language)

emp2.language = "Java"
print(emp2.language, emp2.company)
