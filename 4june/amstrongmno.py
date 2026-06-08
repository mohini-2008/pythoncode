num=int(input("enter a number:"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    sum=sum+rem**3
    temp=temp//10
if num==sum:
    print("Armstrong no:")
else:
    print("Not Armstrong no:")
