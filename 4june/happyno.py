num=20
while num!=1 and num!=4:
    sum=0
    while num>0:
        rem=num%10
        sum=sum+rem*rem
        num=num//10
    num=sum
if num==1:
    print("happy No:")
else:
    print("not happy no:")
        
