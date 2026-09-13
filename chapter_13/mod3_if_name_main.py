"""
📚 Topic: Mod3 If Name Main

This script demonstrates mod3 if name main using conditions, functions and
classes.

💡 Key points:
    1️⃣ the basic syntax for mod3 if name main
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    mod3 if name main affects the result.
"""


class Employee:
    def __init__(self, name, com) -> None:
        self.name = name
        self.company = com

    @staticmethod
    def hello():
        print("Hello Empolyee")

    @property
    def printCompany(self):
        return f"Your company name is {self.company}"


if __name__ == "__main__":
    e1 = Employee("Hamza", "Google")
    e1.hello()
    print(e1.printCompany)
