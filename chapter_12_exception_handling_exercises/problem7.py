"""
📚 Topic: Chapter 12 Exercise - Problem 7

Define and raise a custom `NegativeValueError` when negative numbers
are passed.

💡 Key points:
    1️⃣ Subclassing `Exception` to create `NegativeValueError`
    2️⃣ Raising the custom exception conditionally
    3️⃣ Handling the domain error cleanly in client code
"""


# Define NegativeValueError and raise it when a function receives a negative
# number.
class NegativeValueError(Exception):
    pass


def accept_positive_value(n):
    if n < 0:
        raise NegativeValueError


try:
    n = int(input("Enter a number : "))
    accept_positive_value(n)
except NegativeValueError:
    print("Please Enter positive Number")
