x={}
 key=input("enter a key:")
value=input("enter a value:")
x[key]=value
print(x)

#ADD
x.update(age="18")
x.update({"name":"sita"})
print(x)

stud={
    "name":"ram",
    "age":20,
    "div":"A"
    }
    
#functions
print(stud.keys())
print(stud.values())
print(stud.items())


#looping dictionary
for key,value in stud.items():
    print(key,value)
