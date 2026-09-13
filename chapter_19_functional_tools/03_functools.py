"""
📚 Topic: The functools Module

This script demonstrates common tools from Python's built-in functools
module - reduce, lru_cache, partial, and wraps.

💡 Key points:
    1️⃣ the basic syntax for functools.reduce and functools.partial
    2️⃣ how @lru_cache fits into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    the functools module affects the result.
"""

from functools import reduce, lru_cache, partial, wraps
import time

# ---------------------------------------------------
# reduce() : combines all items in a list into a single value
# ---------------------------------------------------
numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce:", total)

product = reduce(lambda a, b: a * b, numbers)
print("Product using reduce:", product)


# ---------------------------------------------------
# partial() : "pre-fills" some arguments of a function, creating a
# new, simpler version of it
# ---------------------------------------------------
def power(base, exponent):
    return base**exponent


square = partial(power, exponent=2)  # exponent is now always 2
cube = partial(power, exponent=3)  # exponent is now always 3

print("square(5):", square(5))
print("cube(2):", cube(2))


# ---------------------------------------------------
# lru_cache : automatically remembers previous results so the function
# doesn't have to redo slow work twice with the same input
# ---------------------------------------------------
@lru_cache(maxsize=None)
def slow_square(n):
    time.sleep(1)  # pretend this is a slow calculation
    return n * n


start = time.time()
print(slow_square(5))
print("first call took:", time.time() - start, "secs")

start = time.time()
print(slow_square(5))  # instant this time - it's cached!
print("second call took:", time.time() - start, "secs")


# ---------------------------------------------------
# wraps() : fixes a decorator's "identity crisis"
# ---------------------------------------------------
# Without @wraps, a decorated function forgets its own name/docstring
def timer_without_wraps(func):
    def wrapper(*args):
        return func(*args)

    return wrapper


def timer_with_wraps(func):
    @wraps(func)  # this keeps func's original name/docstring
    def wrapper(*args):
        return func(*args)

    return wrapper


@timer_without_wraps
def greet_v1():
    """Greets the user."""
    print("hello")


@timer_with_wraps
def greet_v2():
    """Greets the user."""
    print("hello")


print("Without @wraps, name becomes:", greet_v1.__name__)  # "wrapper"
print("With @wraps, name stays:", greet_v2.__name__)  # "greet_v2"


# ---------------------------------------------------
# 💡 Why this matters for Data Science
# ---------------------------------------------------
# lru_cache is genuinely useful when re-running the same expensive
# calculation (like loading a large file or an API call) multiple
# times during data exploration - it saves you from redoing the wait.


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Forgetting @wraps in your own decorators - this quietly breaks
# debugging tools and documentation that rely on a function's real
# name, since every decorated function would just show up as "wrapper".
