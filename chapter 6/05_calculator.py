print('''
This is calculator which perfomed + - * / ''')
num1=int(input("Enter 1 number : "))
oprator=input("Enter oprator : ")
num2=int(input("Enter 2 number : "))

if (oprator=="+"):
    print("{} + {} = {}".format(num1,num2,num1+num2))

elif (oprator=="-"):
    print("{} - {} = {}".format(num1,num2,num1-num2))
    
elif(oprator=="*"):
    print("{} * {} = {}".format(num1,num2,num1*num2))

elif(oprator=="/"):
    print("{} / {} = {}".format(num1,num2,num1/num2))
print("Thank you for using this calsi")