"""
📚 Topic: Classes and Objects

This script demonstrates classes and objects using for loops, classes and
imports.

💡 Key points:
    1️⃣ the basic syntax for classes and objects
    2️⃣ how for loops fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    classes and objects affects the result.
"""


class Employee:
    salary = 10000  # This is class attribut
    company = "Micosoft"
    language = "Python"


emp1 = Employee()
emp2 = Employee()

emp1.name = "Hamza"  # This is an object/ instance attribut
print(emp1.name, emp1.company, emp1.language)

emp2.name = "Rohan"  # This is an object/ instance attribut
print(emp2.name, emp2.company, emp2.language)
