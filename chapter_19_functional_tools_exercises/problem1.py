"""
📚 Topic: Function Execution Logger Decorator

This script implements a decorator that logs invocation arguments and return
values of wrapped functions.

💡 Key points:
    1️⃣ Capturing `*args` and `**kwargs` inside decorator wrapper
    2️⃣ Inspecting function execution results dynamically
    3️⃣ Preserving return values and exception transparency
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
