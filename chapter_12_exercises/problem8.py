#8 : Define a custom exception class InvalidAgeError without a constructor. Write a program that raises this exception if the user inputs an age below 0 or above 150.
class InvalidAgeError(Exception):
    pass
try:
    user_age=int(input("Enter your age: "))
    if user_age<=0 or user_age>150:
        raise InvalidAgeError
except InvalidAgeError:
    print("Age must be grater then 0 or less 150")

