"""
📚 Topic: Decorators Basics

This script demonstrates what a decorator is, how functions being
first-class citizens makes decorators possible, and the @ syntax
shortcut for applying them.

💡 Key points:
    1️⃣ the basic syntax for writing a wrapper function
    2️⃣ how the @ symbol fits into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    decorators basics affects the result.
"""


# ---------------------------------------------------
# Python functions are "first-class citizens"
# ---------------------------------------------------
# This means a function can be passed around just like any other value
# (a number, a string) - even passed INTO another function as an argument.
def modify(func, num):
    return func(num)


def square(num):
    return num**2


print(modify(square, 2))  # passing square() itself into modify()


# ---------------------------------------------------
# What is a decorator?
# ---------------------------------------------------
# A decorator is a function that takes ANOTHER function as input, adds
# some extra behavior around it, and returns the improved version.
# This is only possible because functions are first-class citizens.
def my_decorator(func):
    def wrapper():
        print("***********************")
        func()
        print("***********************")

    return wrapper


def hello():
    print("hello")


def display():
    print("hello nitish")


# manually wrapping a function with the decorator
a = my_decorator(hello)
a()

b = my_decorator(display)
b()


# ---------------------------------------------------
# The @ syntax - a shortcut for the exact same thing above
# ---------------------------------------------------
def my_decorator(func):
    def wrapper():
        print("***********************")
        func()
        print("***********************")

    return wrapper


@my_decorator
def hello():
    print("hello")


hello()  # calling hello() now automatically runs the wrapper too


# ---------------------------------------------------
# 🆚 Manual wrapping vs @ syntax
# ---------------------------------------------------
# a = my_decorator(hello)   -> manual way, works but repetitive
# a()
#
# @my_decorator
# def hello(): ...          -> same result, but cleaner and reusable
# hello()


# ---------------------------------------------------
# 💡 Why this matters for Data Science
# ---------------------------------------------------
# Decorators like @timer or @log_calls (next file) are used constantly
# in real projects to measure how long a function takes, or to log
# every time a data-processing function runs - without touching the
# original function's code at all.
