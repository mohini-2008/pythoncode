
try:
    a=int(input("enter first number:"))
    b=int(input("enter secont number:"))
    def add(a,b):
        return a+b
    print("Addition =",add(a,b))

except ValueError:
    print("Invalid value")
