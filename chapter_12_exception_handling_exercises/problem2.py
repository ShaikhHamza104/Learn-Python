"""
📚 Topic: Chapter 12 Exercise - Problem 2

Perform arithmetic division handling `ZeroDivisionError` and `ValueError`.

💡 Key points:
    1️⃣ Validating numeric integer conversion
    2️⃣ Catching division by zero attempts
    3️⃣ Providing distinct error messages for each condition
"""


# Prompt for two numbers and perform division. Use separate except blocks
# for ZeroDivisionError and ValueError.


def division_of_two_numbers(a: int, b):
    return a / b


try:
    a = int(input("Enter a first number : "))
    b = int(input("Enter a second number : "))
    division_of_two_numbers(a, b)
except ValueError:
    print("Check input")
except ZeroDivisionError:
    print("You cannot divide any number by zero ")
