# Create a program that prompts the user for two numbers and performs division. Use multiple except blocks to handle ZeroDivisionError and ValueError.

def divisionOfTwoNumber(a:int,b):
    return a/b
try:
    a=int(input("Enter a first number : "))
    b=int(input("Enter a second number : "))
    divisionOfTwoNumber(a,b)
except ValueError:
    print("Check input")
except ZeroDivisionError:
    print("You cannot dived any number by zero ")