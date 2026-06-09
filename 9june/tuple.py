#print type & tuple
"""x=(10,98,90,34,56)
print(x,type(x))

#tuple -> list
l=list(x)
print(l,type(l))

#loop
for i in x:
    print(i)
#min & max    
print("Maximum =",max(x))
print("minimum =",min(x))

#sort
l.sort()
print("Acending order=",l)
#reverse
l.sort(reverse=True)
print("Deceding order=",l)
"""
#nested tuple
x=((10,20,30),40,50,["hello","bye"])
print(x,type(x))
x[3][0]=90
print(x)

#tuple in list
y=[10,[20,30],(60,40)]
y[1][0]=100
print(y)

#print nested tuple
x=((20,40,50),20,50,["hello","bye"])
for i in x:
    if type(i)==tuple:
        for item in i:
            print(item)
    else:
        print()
