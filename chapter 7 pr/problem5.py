# 5. Write a program to find the sum of first n natural numbers using while loop.

num=int(input("Enter numbers : "))
i=0
sum=0
while(i<=num):
    sum+=i
    i+=1
else:
    print("Sum of {0} natural numbers is {1}".format(num,sum))