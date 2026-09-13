"""
📚 Topic: Problem1

This script demonstrates problem1 using decorators, closures and
exception handling.

💡 Key points:
    1️⃣ the basic syntax for problem1
    2️⃣ how decorators fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem1 affects the result.
"""


# 1. Write a decorator called log_call that prints the arguments a
# function was called with, and the value it returned.
def log_call(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(
                f"Called {func.__name__} with args={args}, "
                f"kwargs={kwargs} -> returned {result}"
            )
            return result
        except Exception as e:
            print(f"{func.__name__} raised an error: {e}")

    return wrapper


@log_call
def add(a, b):
    return a + b


@log_call
def divide(a, b):
    return a / b


add(5, 3)
divide(10, 0)
