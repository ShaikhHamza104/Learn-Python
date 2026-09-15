"""
📚 Topic: Method Overloading Patterns in Python

This script explores method overloading patterns in Python using default
arguments and variable-length arguments.

💡 Key points:
    1️⃣ Python does not support duplicate method definitions with varied types
    2️⃣ Later method definitions silently overwrite earlier ones
    3️⃣ Handling variable parameters with default `None` arguments or `*args`

🧠 Beginner tip:
    For true static type-based overloading, use the `@typing.overload`
    decorator from the standard library.
"""


class Addition:
    def sum(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return f"{a}+{b}+{c}={a+b+c}"

        elif a is not None and b is not None:
            return f"{a}+{b}={a+b}"

        elif a is not None:
            return f"{a} = {a}"

        else:
            print("Check the enter you ")


o = Addition()
print(o.sum(12, 2))
print(o.sum(11, 9))
print(o.sum(10))
