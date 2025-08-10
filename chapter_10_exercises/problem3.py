# 3. Create a class with a class attribute a; create an object from it and set ‘a’  directly using ‘object.a = 0’. Does this change the class attribute

class A:
    a=10
o=A()
# o.a=0
print(o.a)