# 6. Write a program to calculate the factorial of a given number using for loop.
num=int(input("Enter number : "))
fact=1
for i in range(1,num+1):
    fact=fact*i
else:
    print(f"factorial of {num} is {fact}")