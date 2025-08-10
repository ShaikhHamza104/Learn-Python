year=int(input("Enter year : "))
if (year%4==0):
    if year%100==0:
        if year%400==0:
            print("Year is leap year")
        else:
            print("Year is not Leap year")
    else:
        print("Year is Leap year")
else:
    print("Year is not Leap year")