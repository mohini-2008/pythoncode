x=frozenset([10,20,30])
print(x,type(x))

for i in x:
    print(i)
    
print(200 in x)

x=frozenset((10,30,50))
print(x,type(x))

x=frozenset("hello")
print(x,type(x))

x=frozenset({101:"sam",102:"arya"})
print(x,type(x))
