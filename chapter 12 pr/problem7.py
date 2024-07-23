#  Define a custom exception NegativeValueError. Write a function that raises this exception if a negative number is passed to it.
class NegativeValueError(Exception):
    pass

def acceptPositiveValue(n):
    if n<0:
        raise NegativeValueError
    

try:
    n=int(input("Enter a number : "))
    acceptPositiveValue(n)
except NegativeValueError:
    print("Please Enter positive Number")