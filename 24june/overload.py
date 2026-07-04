class demo:
    def add(self,a,b,c=0):
        return a+b+c
d=demo()
print(d.add(10,20))
print(d.add(10,20,30))
