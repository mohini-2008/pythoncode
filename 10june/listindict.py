
#list in dict
stud={
    "name":"ram",
    "age":20,
    "div":"A",
    "Marks":[100,87,98],
    "sub":["C","C++","Python"],
    "roll":59
    }
    
for values in stud.values():
    if type(values)==list:
        for i in values:
            print(i)
        continue
    print(values)
