"""
📚 Topic: Call Limiter Decorator Factory

This script implements a parameterized decorator factory that enforces a
maximum call limit on functions.

💡 Key points:
    1️⃣ Three-level nested function structure for parameterized decorators
    2️⃣ Tracking stateful call counts across invocations
    3️⃣ Preserving function metadata using `@functools.wraps`
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
                        f"{func.__name__} can only be called {limit} "
                        f"time(s)"
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
