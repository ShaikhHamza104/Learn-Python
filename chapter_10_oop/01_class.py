"""
📚 Topic: Classes and Objects

This script introduces Object-Oriented Programming (OOP) in Python, creating
classes as blueprints and instantiating objects.

💡 Key points:
    1️⃣ Defining classes with the `class` keyword (PascalCase convention)
    2️⃣ Defining class attributes shared across all instances
    3️⃣ Instantiating objects and accessing their attributes

🧠 Beginner tip:
    A class is the architectural blueprint; an object is an individual
    building constructed from that blueprint.
"""


class Employee:
    salary = 10000  # This is class attribute
    company = "Microsoft"
    language = "Python"


emp1 = Employee()
emp2 = Employee()

emp1.name = "Hamza"  # This is an object/ instance attribute
print(emp1.name, emp1.company, emp1.language)

emp2.name = "Rohan"  # This is an object/ instance attribute
print(emp2.name, emp2.company, emp2.language)
