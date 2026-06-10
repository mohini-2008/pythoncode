x=set()
print(type(x))
x.add(30)
print(x)

x={10,30,40,20,10}
print(x)

#set to list
x1=list(x)
print(x1[0])

x1[2]=90
print(x1)

#list to set
x=set(x1)
print

#SET FUNCTION
A={1,2,3}
B={3,4,5}

print(A|B)#union
print(A&B)#intersetcion
print(A-B)#difference
print(A^B)#symentric difference
