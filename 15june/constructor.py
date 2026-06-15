class demo:
    c_name="abc"
    #default constructor
    def __init__(self):
        print("Defult constructor class:")
        
#1st way CLASSNAME
print(demo.c_name)

#2nd way OBJET
D=demo()
print(D.c_name)
    
#PARAMETERIZED CONSTRUCTOR

class stud():
    def __init__(self):
        self.name="ram"
        self.Roll=59

s=stud()#obj creation
print(s.name)
s.name="samu"#changing value
print(s.name)
print(s.Roll)



class student():
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        
s=student("sita",89)
print(s.name)
print(s.roll)
