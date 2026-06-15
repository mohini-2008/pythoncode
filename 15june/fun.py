#without argument
def greet():
    print("Hello")
greet()

#with argument
def cube(num):
    print(num*num*num)
n=int(input("enter a no:"))
cube(n)

#with argumengt & return type
def getno():
    return 10
#1st way
op=getno()
print(op)

#2nd way
print(getno())

def add(a,b):
    return a+b
print(add(10,30))
print(add(10.0,56.3))
