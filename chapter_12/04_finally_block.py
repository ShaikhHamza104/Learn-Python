add = lambda a,b : a+b
sub = lambda a,b : a-b
mul = lambda a,b : a*b
div = lambda a,b : a/b

opration={
    "+":add,
    "-":sub,
    "x":mul,
    "/":div
}

try:
    a=int(input("Enter first number: "))

    for oprator in opration:
        print(oprator)
    o=input("Enter oprator ")
    b=int(input("Enter second number: "))

    
except ValueError:
    print("Please check your inputs ")

except KeyError:
    print("Please enter a valid oprator ")

else:
    if o=="+":
        print(f"Addition of {a} and {b}",add(a,b))

    elif o=="-":
        print(f"Subtraction of {a} and {b}",sub(a,b))

    elif o=="*":
        print(f"Multiplication of {a} and {b}",mul(a,b))

    elif o=="/":
        print(f"Division of {a} and {b}",div(a,b))

finally:
    print("Thanks for using calculator")