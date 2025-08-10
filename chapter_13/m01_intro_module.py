class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self,a,b):
        return f"Addition of {a} and {b} is {a+b}"

    def sub(self,a,b):
        return f"Subtraction of {a} and {b} is {a-b}"    

    def mul(self,a,b):
        return f"Multiplication of {a} and {b} is {a*b}"

    def div(self,a,b):
        return f"Division of {a} and {b} is {(a/b):.2f}"
    