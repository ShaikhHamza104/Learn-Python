# Write a program which finds out whether a given name is present in a list or not.
list_of_name=["Rohit","Rajo","Harry","Hamza"]
name=input("Enter your name : ").capitalize()
if name in list_of_name:
    print("Your name in the list")
else:
    print("Your name not in the list")
