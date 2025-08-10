height=int(input("Enter your height in cm : "))
bill=0
if height>=120:
    print("You can ride")
    age=int(input("Enter your age : "))
    if age<12:
        print("You can pay 5$")
        bill=5  
    elif  age<=18:
        print("You can pay 7$")
        bill=7  
    elif age>18:
        print("You can pay 12$")
        bill=12  
    photo=input("you want to take a photo ")
    if photo=='yes' or photo=='y':
        print("You can pay 3$")
        bill+=3
    
    print(f"Your total bill is {bill}")  
else:
    print("You can not ride")