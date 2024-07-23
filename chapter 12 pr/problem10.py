# 10.Create a program that continuously prompts the user to enter two numbers and performs division. Use exception handling to manage ZeroDivisionError and provide a meaningful error message. Allow the user to exit the loop by entering a specific keyword.
def divding_by_0():
    try:
        a=int(input("Enter a first number: "))
        b=int(input("Enter a second number: "))
        d=a/b
    except ZeroDivisionError:
        print(f"You can {a} by deviding by 0")
    else:
        print(f"Division of deviding {a} by {b} is {d}")
divding_by_0()