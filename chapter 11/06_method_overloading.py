class Addition:
    def sum(self,a=None,b=None,c=None):
        if a is not None and b is not None and c is not None :
            return f"{a}+{b}+{c}={a+b+c}"

        elif a is not None and b is not None:
            return f"{a}+{b}={a+b}"
        
        elif a is not None:
            return f"{a} = {a}"
        
        else:
            print("Check the enter you ")
o=Addition()
print(o.sum(12,2))
print(o.sum(11,9))
print(o.sum(10))