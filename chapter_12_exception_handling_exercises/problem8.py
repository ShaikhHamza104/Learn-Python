"""
📚 Topic: Chapter 12 Exercise - Problem 8

Validate user passwords against length constraints using custom exceptions.

💡 Key points:
    1️⃣ Defining custom validation exceptions
    2️⃣ Checking string length conditions
    3️⃣ Enforcing minimum security criteria
"""


# Define InvalidAgeError without a constructor. Raise it for an age below 0
# or above 150.
class InvalidAgeError(Exception):
    pass


try:
    user_age = int(input("Enter your age: "))
    if user_age <= 0 or user_age > 150:
        raise InvalidAgeError
except InvalidAgeError:
    print("Age must be grater then 0 or less 150")
