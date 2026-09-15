"""
📚 Topic: Multilevel Inheritance

This script demonstrates multilevel inheritance where a class inherits from a
derived class, forming a vertical hierarchy chain.

💡 Key points:
    1️⃣ Linear class hierarchy: `GrandChild -> Child -> Parent`
    2️⃣ Inheriting cumulative capabilities down the chain
    3️⃣ Accessing grand-parent attributes from the grand-child class

🧠 Beginner tip:
    Keep inheritance chains shallow (2-3 levels maximum) to maintain
    readability and ease of debugging.
"""


class A:
    first = 0

    def get_value_a(self):
        # global first
        self.first = int(input("Enter first number "))

# B class inherit A class


class B(A):
    second = 0

    def get_value_b(self):
        # global second
        self.second = int(input("Enter second number "))

# C class inherit B class


class C(B):
    def sum(self):
        return self.first + self.second

    def minus(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


o = C()
o.get_value_a()
o.get_value_b()
print("Sum is ", o.sum())
print("Minus is ", o.minus())
print("Multiply is ", o.mul())
print("Division is ", o.div())
