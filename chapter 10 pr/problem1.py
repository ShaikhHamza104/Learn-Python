# . Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    comany="Microsoft" #class attribute
    l=['harry','Rehan',"Aman"]
    def detailInfo(self):
        for name in self.l:
            print("The name of employee is "+name.capitalize()+" and capany is "+self.comany)
obj=Programmer()
obj.detailInfo()