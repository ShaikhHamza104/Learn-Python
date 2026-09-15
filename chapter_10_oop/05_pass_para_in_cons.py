"""
📚 Topic: Parameterized Constructors

This script demonstrates passing arguments through `__init__` to customize each
object during instantiation.

💡 Key points:
    1️⃣ Defining constructor parameters after `self`
    2️⃣ Binding incoming arguments to instance attributes: `self.name = name`
    3️⃣ Creating diverse, distinct object instances from one class

🧠 Beginner tip:
    Default parameter values can be assigned in `__init__` to make constructor
    arguments optional.
"""


class Employee:
    def __init__(self, name, lan, company):
        self.name = name
        self.language = lan
        self.company = company
        print(self.name, self.language, self.company)


emp = Employee("Hamza", "Python", "Microsoft")
