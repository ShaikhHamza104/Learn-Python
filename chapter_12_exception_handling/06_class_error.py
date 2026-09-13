"""
📚 Topic: 06 Class Error

This script demonstrates 06 class error using functions, classes and
exception handling.

💡 Key points:
    1️⃣ the basic syntax for 06 class error
    2️⃣ how functions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    06 class error affects the result.
"""


class Empolyee:
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company

    def show(self):
        print(
            f"The name of employee is {self.name}.\n"
            f"Age of employee is {self.age}, and his working in {self.company}"
        )


e1 = Empolyee(name="Hamza", age=18, company="Google")
try:
    print(e1.gender)
except AttributeError:
    print("This attribute not define in this class ")
e1.show()
