start=int(input("enter starting value:"))
end=int(input("enter ending value:"))
for i in range(start,end+1):
    if i%2==0 and i%6==0:
        print(i)
