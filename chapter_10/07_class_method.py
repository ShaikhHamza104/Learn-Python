"""
📚 Topic: Class Methods

This script demonstrates class methods using functions and classes.

💡 Key points:
    1️⃣ the basic syntax for class methods
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    class methods affects the result.
"""


class Employee:
    company = "Microsoft"

    @classmethod
    def changeCompany(cls, company):
        cls.company = company


e = Employee()
print(e.company)
e.changeCompany("Gooogle")
print(e.company)
