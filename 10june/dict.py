#type
x={}
print(x,type(x))

#add key
x["name"]="Samiksha"
print(x)
print(x["name"])

#update
x["name"]="Arya"
print(x)
x[101]="stud data"
print(x)

#DEL 
del x[101]
print(x)

#POP
print(x.pop("name")) #while print the deleted value
print(x)
