l=[1,2,3,4]
try:
    user_input=int(input("Enter a number between 0 and 3: "))
    i=0
    while i<user_input:
        print(l[user_input]) 
        i+=1
except ValueError :
    print("Enter a valid number not character or floting point number")
except IndexError:
    print("Enter value not be grater then ",len(l)-1)