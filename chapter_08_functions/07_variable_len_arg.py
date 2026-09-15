"""
📚 Topic: Variable-Length Arguments (*args and **kwargs)

This script demonstrates accepting arbitrary numbers of positional and
keyword arguments.

💡 Key points:
    1️⃣ `*args`: packs extra positional arguments into a tuple
    2️⃣ `**kwargs`: packs extra keyword arguments into a dictionary
    3️⃣ Writing flexible functions that adapt to variable inputs

🧠 Beginner tip:
    The asterisks `*` and `**` perform the packing/unpacking; `args` and
    `kwargs` are standard conventional names.
"""


def add(*args):
    return sum(args)


result = add(1, 2, 3, 4)  # *args collects all positional arguments into a
# tuple
print(result)  # Output: 10


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_details(name="Alice", age=30, city="New York")  # **kwargs collects all
# keyword arguments into a dictionary
# Output:
# name: Alice
# age: 30
# city: New York
