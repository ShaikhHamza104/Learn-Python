"""
📚 Topic: Chapter 10 Exercise - Problem 3

Demonstrate whether setting an instance attribute alters a class attribute.

💡 Key points:
    1️⃣ Defining a class attribute `a = 10`
    2️⃣ Setting instance attribute `o.a = 0` creates an instance attribute
    3️⃣ Verifying that class attribute `A.a` remains unchanged
"""


class A:
    a = 10


o = A()
# o.a=0
print(o.a)
