# 1.Write a Python program that takes an integer input from the user and raises a ValueError if the input is not an integer.
def inputAsInteger():
    try:
        n=int(input("Enter any number "))
    except ValueError as e:
        print(e)
inputAsInteger()
