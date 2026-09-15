"""
📚 Topic: The `finally` Block & Guaranteed Cleanup

This script demonstrates the `finally` clause, which executes unconditionally
whether an exception was raised, caught, or not.

💡 Key points:
    1️⃣ `finally` runs regardless of whether exceptions were encountered
    2️⃣ Guaranteed execution even if blocks contain `return` or `break`
    3️⃣ Standard tool for releasing locks, database handles, and sockets

🧠 Beginner tip:
    Use `finally` for mandatory cleanup actions that must always occur.
"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

try:
    a = int(input("Enter first number: "))

    for operator in operations:
        print(operator)
    o = input("Enter operator: ")
    b = int(input("Enter second number: "))

    if o not in operations:
        raise KeyError(f"Invalid operator: {o}")

except ValueError:
    print("Please check your inputs.")

except KeyError:
    print("Please enter a valid operator.")

else:
    calc_func = operations[o]
    print(f"Result of {a} {o} {b} =", calc_func(a, b))

finally:
    print("Thanks for using calculator")
