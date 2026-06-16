class abc:
    msg = "samiksha"
    
    @classmethod
    def display_classvar(cls):
        return cls.msg
        
    def __init__(self,age):
        self.name="neha"
        self.age = age
        
    def display(self):
        print("name is ",(self.name),"and age is",(self.age))
        
    @staticmethod
    def greet(name,objref):
        return f"hello gm{name}{abc.msg}{objref.age}"
obj=abc(29)    
obj.display()
print(obj.display_classvar())
print(abc.greet("ram",obj))
