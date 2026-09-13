"""
📚 Topic: Problem3

This script demonstrates problem3 using decorator factories, functools
and exception handling.

💡 Key points:
    1️⃣ the basic syntax for problem3
    2️⃣ how functools.wraps fit into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    problem3 affects the result.
"""

from functools import wraps


# 3. Write a decorator factory called max_calls(limit) that only lets
# a function run a certain number of times, then raises an error on
# any further calls.
def max_calls(limit):
    def decorator(func):
        call_count = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_count
            try:
                if call_count >= limit:
                    raise PermissionError(
                        f"{func.__name__} can only be called {limit} " f"time(s)"
                    )
                call_count += 1
                return func(*args, **kwargs)
            except PermissionError as e:
                print(e)

        return wrapper

    return decorator


@max_calls(2)
def greet(name):
    print(f"Hello, {name}!")


greet("Hamza")  # 1st call - works
greet("Ali")  # 2nd call - works
greet("Sara")  # 3rd call - blocked

print("Function name is still:", greet.__name__)  
# thanks to @wraps
