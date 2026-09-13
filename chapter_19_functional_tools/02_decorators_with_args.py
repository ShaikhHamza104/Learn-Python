"""
📚 Topic: Decorators With Arguments

This script demonstrates how to write decorators that work on
functions which take arguments, and decorators that take their own
configuration arguments.

💡 Key points:
    1️⃣ the basic syntax for *args inside a wrapper
    2️⃣ how a decorator factory (a decorator that takes arguments) fits in
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    decorators with arguments affects the result.
"""

import time


# ---------------------------------------------------
# Problem: our first decorator only worked on functions with NO arguments
# ---------------------------------------------------
# Fix: use *args inside the wrapper to accept ANY number of arguments
# and pass them straight through to the real function.
def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print("time taken by", func.__name__, time.time() - start, "secs")

    return wrapper


@timer
def hello():
    print("hello world")
    time.sleep(1)


@timer
def square(num):
    time.sleep(1)
    print(num**2)


@timer
def power(a, b):
    print(a**b)


hello()
square(2)
power(2, 3)


# ---------------------------------------------------
# A decorator that takes its OWN arguments (a "decorator factory")
# ---------------------------------------------------
# This is a decorator that first needs a setting (like a data type to
# check for) before it can decorate a function. That means we need
# THREE layers of functions instead of two.
def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args) == data_type:
                func(*args)
            else:
                raise TypeError("This data type is not allowed here")

        return inner_wrapper

    return outer_wrapper


@sanity_check(int)
def square(num):
    print(num**2)


@sanity_check(str)
def greet(name):
    print("hello", name)


square(2)  # works - 2 is an int
greet("Hamza")  # works - "Hamza" is a str
# square("2")       # would raise TypeError - "2" is a str, not an int


# ---------------------------------------------------
# 🆚 Normal decorator vs decorator factory
# ---------------------------------------------------
# @timer                  -> a normal decorator, used directly
# @sanity_check(int)       -> a decorator FACTORY - it needs () with a
#                             setting before it can be used as a decorator


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Forgetting the extra layer of function when writing a decorator
# factory. Remember the order: settings -> the real decorator -> the
# wrapper. Three functions deep, not two.
