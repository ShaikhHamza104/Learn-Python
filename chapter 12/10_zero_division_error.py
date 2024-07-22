try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=a/b
except ValueError:
    print("Please enter a valid number ")

except ZeroDivisionError:
    print("You can try to dividing number by 0")

else:
    print(c)