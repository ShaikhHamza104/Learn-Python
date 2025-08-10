print("Welcom to the trip calculator!")
bill=float(input("What was the total $"))#150$
tip=int(input("How much tip would you like to give? 10,12 or 15 "))#(tip/100)
people=int(input("How many people to the split "))
total_bill=(bill+(bill*(tip/100)))/people
finall_bill="{:.2f}".format(total_bill)
print(f"Each person should pay: {finall_bill}")