"""
📚 Topic: Keyword Arguments

This script demonstrates passing arguments by parameter name rather than by
their position.

💡 Key points:
    1️⃣ Supplying arguments as `name=value` pairs
    2️⃣ Calling arguments in any order when keyword names are provided
    3️⃣ Combining clarity with readability in multi-parameter calls

🧠 Beginner tip:
    Positional arguments must always come before keyword arguments in a
    function call.
"""


def print_sum(a, b, c, d):
    print(f"{a} + {b} + {c} + {d} = {a+b+c+d}")


print_sum(a=10, b=20, c=30, d=40)
