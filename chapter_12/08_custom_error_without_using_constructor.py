class InvalidAge(Exception):
    pass
try:
    age=int(input("Enter your age : "))
    if age<18:
        raise InvalidAge
except InvalidAge:
    print("Age should not be less then 18 ")