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

# Logical not 
print(not(False))
print(not(True))

# 5. membership Operators
l=[1,2,3]
# membership "in"  Operator
print(1 in l)
# membership "not in"  Operator
print(0 not in l)

# 6. Identity Operators
a=10
b=10
# Identity "is" Operator
print("a is b",a is b)
# Identity "is not" Operator
print("a is not b",a is not b)

# 7. Bitwise Operators
# Bitwise AND
a = 12  # binary: 1100
b = 10  # binary: 1010
result = a & b  # binary: 1000, decimal: 8
print("AND operation:", result)

# Bitwise OR
result = a | b  # binary: 1110, decimal: 14
print("OR operation:", result)

# Bitwise XOR
result = a ^ b  # binary: 0110, decimal: 6
print("XOR operation:", result)

# Bitwise NOT
result = ~a  # binary: ...11110011 (in a 32-bit system), decimal: -13
print("NOT operation:", result)

# Left Shift
result = a << 2  # binary: 110000, decimal: 48
print("Left Shift operation:", result)

# Right Shift
result = a >> 2  # binary: 0011, decimal: 3
print("Right Shift operation:", result)