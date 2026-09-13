"""
📚 Topic: Method Overloading Concepts

This script demonstrates method overloading concepts using conditions,
functions and classes.

💡 Key points:
    1️⃣ the basic syntax for method overloading concepts
    2️⃣ how conditions fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    method overloading concepts affects the result.
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
