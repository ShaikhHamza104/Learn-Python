class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class B(A):
    def __init__(self, a, b):
        super().__init__(a, b)
        print(a+b)
o=B(10,20)