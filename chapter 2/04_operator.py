# 1. Arithmetic operators: +, -, *, / etc.
a=10
b=5
print("a + b = ",a+b)
print("a - b = ",a-b)
print("a * b = ",a*b)
print("a / b = ",a/b)

# 2. Assignment operators: =, +=, -= etc.
b+=5
print("b+=5",b)
b-=5
print("b-=5",b)
b*=5
print("b*=5",b)
b/=5
print("b/=5",b)
b**=2
print("b**=5",b)
b//=5
print("b//=5",b)

# 3. Comparison operators: ==, >, >=, <, != etc.
print("a==b",a==b)
print("a>b",a>b)
print("a>=b",a>=b)
print("a<b",a<b)
print("a<=b",a<=b)
print("a!=b",a!=b)

# 4. Logical operators: and, or, not.
a=True
b=False
print("a and b",a and b)
print("a or b" ,a or b)
print("not a", not a)

# Truth table of 'and'
print("Ture and False",True and False)
print("Ture and True",True and True)
print("False and True",False and True)
print("False and False",False and False)

# Truth table of 'or'

print("Ture or False",True or False)
print("Ture or True",True or True)
print("False or True",False or True)
print("False or False",False or False)

print(not(False))
print(not(True))
# 5. membership Operators
l=[1,2,3]
print(1 in l)
print(0 not in l)

# 6. Identity Operators
a=10
b=10
print("a is b",a is b)
print("a is not b",a is not b)