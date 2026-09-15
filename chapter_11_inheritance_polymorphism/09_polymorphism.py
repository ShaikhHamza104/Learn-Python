"""
📚 Topic: Polymorphism & Duck Typing

This script demonstrates polymorphism: different classes implementing the same
interface, allowing unified processing.

💡 Key points:
    1️⃣ Treating different objects uniformly through shared method names
    2️⃣ Duck typing: "If it walks and quacks like a duck, it's a duck"
    3️⃣ Decoupling client code from concrete implementations

🧠 Beginner tip:
    In Python, polymorphism does not require a common base class; matching
    method names and signatures is sufficient.
"""


class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
