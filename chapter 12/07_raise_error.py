try:
    age=int(input("Enter your age "))
    if age<18:
        raise ValueError
except ValueError:
    print("Your age is less then 18 ")