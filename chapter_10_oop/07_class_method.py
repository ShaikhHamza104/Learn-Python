"""
📚 Topic: Class Methods (`@classmethod`)

This script demonstrates methods that receive the class object (`cls`) rather
than an individual instance (`self`).

💡 Key points:
    1️⃣ Decorated with `@classmethod`
    2️⃣ Receives the class as its first parameter (`cls`)
    3️⃣ Capable of modifying class-level state across all instances

🧠 Beginner tip:
    Class methods are frequently used as factory methods (alternative
    constructors) for creating objects from different data formats.
"""


class Employee:
    company = "Microsoft"

    @classmethod
    def change_company(cls, company):
        cls.company = company


e = Employee()
print(e.company)
e.change_company("Google")
print(e.company)
