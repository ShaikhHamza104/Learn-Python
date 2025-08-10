# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
mark1=int(input("Enter your mark "))
mark2=int(input("Enter your mark "))
mark3=int(input("Enter your mark "))
percentage=(100*(mark1+mark2+mark3))/300
if (percentage>40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You are pass ",percentage)
else:
    print("You Failed ,try again next year ",percentage)
