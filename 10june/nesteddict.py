product={
    101:{
        "productname":"car",
        "price":10000,
        "color":"black",
        "qty":10,
        "model":[501,502]
    }
}
print(product[101])
print(product[101]["color"])

#key
for v in product.values():
    for k in v.values():
        print(k)
product={
    101:{
        "productname":"car",
        "price":10000,
        "color":"black",
        "qty":10,
        "model":[501,502]
    }
}
print(product[101])
print(product[101]["color"])

#key
for v in product.values():
    for k,v in v.items():
        print(k,v)
    

        

    
