num=int(input("enter a number:"))
if num>1:
   for i in range(2,num):
         if num%i==0:
             print("prime number:")
             break
         else:
             print("Not prime:")
else:
    print("not prime")
