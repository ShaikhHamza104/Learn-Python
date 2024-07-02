# Write a program to find the greatest of four numbers entered by the user.

num1=int(input("Enter number : "))
num2=int(input("Enter number : "))
num3=int(input("Enter number : "))
num4=int(input("Enter number : "))

if (num1>num2 and num1>num3 and num1>num4):
    print("Number 1 is greater",num1)

elif (num2>num1 and num2>num3 and num2>num4):
    print("Number 2 is greater",num2)

elif (num3>num1 and num3>num2 and num3>num4):
    print("Number 2 is greater",num3)

elif (num4>num1 and num4>num2 and num4>num3):
    print("Number 2 is greater",num4)