print("start")
try:
    a = int(input("enter a :" ))
    b = int(input("enter b :"))
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("invalid value")
    

try:
    ip = int(input("enter number : "))
    print(ip)
except ValueError:
    print("enter number only!")
try:
    x=[10,20,30]
    print(x[7])
except:     
    

try:
    a={"name":"ram"}
    print(a["name"])
    print(a["age"])
        
except Exception as e:
    print("key not present")
else:
    print("end")
finally:
    print("------")
    
