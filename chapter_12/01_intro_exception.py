# This code gernate an Error if the user enter an string or name or character or floating point number
# a=int(input("Enter a number : "))

try:
    a=int(input("Enter a number : "))
except:
    print("Error !! Please enter a valid number ")