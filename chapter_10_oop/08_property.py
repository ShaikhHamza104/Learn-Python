"""
📚 Topic: The `@property` Decorator

This script demonstrates Python's `@property` decorator to expose getter
methods with clean, attribute-like access syntax.

💡 Key points:
    1️⃣ Transforming method calls into attribute access: `obj.value`
    2️⃣ Encapsulating private or protected storage attributes (`self._value`)
    3️⃣ Providing read-only attributes or computed properties

🧠 Beginner tip:
    Use `@property` to add validation or computed behavior to existing
    attributes without breaking existing client code.
"""


class MyClass:
    def __init__(self, value):
        self._value = value

    # Access method as a property attribute
    @property
    def value(self):
        return self._value


o = MyClass(10)
print(o.value)
