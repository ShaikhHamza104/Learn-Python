print("Thank you for choosing python pizza Deliveries!")
size=input("what size pizza do you want? S, M, or L ").capitalize()
add_pepperoni=input("do you want pepperoni? Y or N ").capitalize()
extra_cheese=input("do you want extra cheese? Y or N ").capitalize()
prize=0
if(size=='S'):
    prize=15
elif(size=="M"):
    prize=20
elif(size=="L"):
    prize=25
if add_pepperoni=="Y":
    prize+=2
if extra_cheese=="Y":
    prize+=1
print("You total bill is {}".format(prize))