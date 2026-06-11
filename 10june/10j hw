stud={
    101: {
        "name":"Ram",
        "age":18,
        "sub":["Python","java","Mean"],
        "marks":[30,89,78]
    },
    102: {
        "name":"sita",
        "age":19,
        "sub":["Python","java","Mean"],
        "marks":[70,80,90],
    },
    103:{
        "name":"Rahul",
        "age":20,
        "sub":["Python","java","Mean"],
        "marks":[58,79,90],
    },
    104: {
        "name":"arya",
        "age":21,
        "sub":["Python","java","Mean"],
        "marks":[88,97,100]
    }
}
#total of all marks
print("roll no\tname\ttotal")
for k , v in stud.items():
    t = sum(v["marks"])
    print( k  , "\t" , v["name"], "\t" , t)

#topper name
t = ""
h = 0
for v in stud.values():
    t = sum(v["marks"])
    if t > h:
        h = t
        t = v["name"]
print("topper is : ",t)

#highest marks in python

h = 0
n =  ""

for v in stud.values():
    pm = v["marks"][0]

    if pm > h:
        h = pm
        n = v["name"]

print("Highest Python Marks =", h)
print("Student Name =", n)

# Name and age gre 19

for v in stud.values():
    if v["age"] > 19:
        print(v["name"], v["age"])
        
# print name whos marks is between 70 ad 90

print("Student Names Having Total Marks > 70 and < 90 :")

for v in stud.values():
    t = sum(v["marks"])

    if t > 70 and t < 90:
        print(v["name"])
