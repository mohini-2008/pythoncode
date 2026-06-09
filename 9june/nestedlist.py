x =[ [1,"toy car",500],
[2,"doll",1000],
[3,"grocery",2000],
[4,"sunglass",5000]
]

print(x[0][1])
#price
for ids in x:
    print(ids[2])
#view   
for i in x:
    print(i)
print()

#Apped
no=int(input("how many time doo you want to add product:"))
for i in range(no):
    product=input("enter product name : ")
    price=float(input("enter price:"))
    id=len(x)+1
    x.append([id,product,price])
for y in x:
    print(y)

#update


        
    
    
    
