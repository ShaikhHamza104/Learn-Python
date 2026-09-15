"""
📚 Topic: The `if __name__ == '__main__'` Idiom

This script demonstrates separating standalone executable code from reusable
imported module code using Python's `__name__` variable.

💡 Key points:
    1️⃣ When run directly, Python sets `__name__` to `'__main__'`
    2️⃣ When imported as a module, `__name__` is set to the module's name
    3️⃣ Prevents test runs and script side effects from running on import

🧠 Beginner tip:
    Always guard top-level execution code with `if __name__ == '__main__':`
    in library modules.
"""


class Employee:
    def __init__(self, name, com) -> None:
        self.name = name
        self.company = com

    @staticmethod
    def hello():
        print("Hello Employee")

    @property
    def company_info(self):
        return f"Your company name is {self.company}"


if __name__ == "__main__":
    e1 = Employee("Hamza", "Google")
    e1.hello()
    print(e1.company_info)
