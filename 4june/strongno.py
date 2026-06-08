num=int(input("enter a number:"))
temp=num
sum=0
while num>0:
    digit=num%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum+=fact
    num//=10
if temp==sum:
    print("Strong number:")
else:
    print("Not a strong number:")
