# syntax:
# if (condition):
#   statement
# elif(condition)
#   statement
# else:
#   statement
age=int(input("Enter your age : "))
if age<18:
    print("You can not take vote")
elif age<=0:
    print("Youre age is invalid .....")
else:
    print("You can take vote")