import m01_intro_module 
a=int(input("Enter number "))
b=int(input("Enter number "))
c=m01_intro_module.Calculator(a,b)
print(c.add(a,b))
print(c.sub(a,b))
print(c.mul(a,b))
print(c.div(a,b))