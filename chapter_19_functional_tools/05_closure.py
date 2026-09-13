"""
📚 Topic: Closures

This script demonstrates what a closure is, how a nested function can
"remember" values from its enclosing function even after that function
has finished running, and why this is the secret behind decorators.

💡 Key points:
    1️⃣ the basic syntax for returning a function from a function
    2️⃣ how the enclosing scope fits into the example
    3️⃣ what to look for when you run the file

🧠 Beginner tip:
    Run this file, change one small value, and run it again to see how
    closures affects the result.
"""


# ---------------------------------------------------
# What is a closure?
# ---------------------------------------------------
# A closure is a function that "remembers" the variables from the
# scope it was created in, even after that outer function has already
# finished running.
def outer():
    message = "Hi Hamza"

    def inner():
        print(message)  # inner() remembers 'message' from outer()

    return inner  # notice: we return inner ITSELF, not inner()


my_func = outer()  # outer() has already finished running by this point...
my_func()  # ...but inner() still remembers 'message'!


# ---------------------------------------------------
# Proof: the outer function's variable stays alive inside the closure
# ---------------------------------------------------
def outer(x):
    def inner(y):
        return x + y  # x comes from outer(), y comes from inner()

    return inner


add_five = outer(5)  # x is now permanently locked in as 5
add_ten = outer(10)  # a separate closure, x is locked in as 10

print(add_five(2))  # 5 + 2 = 7
print(add_ten(2))  # 10 + 2 = 12
# each closure keeps its OWN copy of x - they don't interfere


# ---------------------------------------------------
# A practical example: a counter that remembers its own count
# ---------------------------------------------------
def make_counter():
    count = 0

    def counter():
        nonlocal count  # needed to MODIFY the enclosing variable
        count += 1
        return count

    return counter


counter1 = make_counter()
print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

counter2 = make_counter()  # a brand new, separate closure
print(counter2())  # 1 - counter2 has its own independent count


# ---------------------------------------------------
# A practical example: a multiplier factory
# ---------------------------------------------------
def make_multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15


# ---------------------------------------------------
# 🔗 The connection to decorators
# ---------------------------------------------------
# Every decorator you've written so far is actually a closure:
def my_decorator(func):
    def wrapper():
        print("before the function runs")
        func()  # wrapper "remembers" func from my_decorator
        print("after the function runs")

    return wrapper


@my_decorator
def say_hello():
    print("hello!")


say_hello()
# wrapper() only works because it's a CLOSURE that remembers 'func'
# from my_decorator's scope - this is exactly what you practiced above


# ---------------------------------------------------
# 🆚 Nested function vs Closure
# ---------------------------------------------------
# A nested function is just a function defined inside another function.
# It only BECOMES a closure once it's returned and used OUTSIDE the
# outer function, while still remembering the outer function's variables.


# ---------------------------------------------------
# ⚠️ Common mistake
# ---------------------------------------------------
# Forgetting 'nonlocal' when trying to CHANGE (not just read) a
# variable from the enclosing scope inside a closure - without it,
# Python creates a new local variable instead, and your counter would
# never actually go up.
