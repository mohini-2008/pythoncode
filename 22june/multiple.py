class p1:
    def xyz(self):
        print("from p1 xyz:")
    
    def show(self):
        print("from p1 show:")

    def __init__(self,name):
        self.name=name
        print("p1 constructor")
        print(self.name)

class p2:
    def xyz(self):
        print("from p2 xyz")
    
    def show(self):
        print("from p2 show:")
    def __init__(self,age):
        self.age=age
        print("p2 constructor")
        print(self.age)
    
class c(p1,p2):
    def pqr(self):
        print("child class:")
    
    def call_p2_show(self):
        return p2.show(self)

    def __init__(self,name,age):
        print("c constructor")
        p1.__init__(self,name)
        p2.__init__(self,age)

    

obj=c("ram",20)
obj.xyz()
obj.xyz()
obj.pqr()
obj.show() 
obj.call_p2_show()


