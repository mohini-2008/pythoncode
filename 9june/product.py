products = [
    [1, "Toy Car", 500],
    [2, "Doll", 1000],
    [3, "Grocery", 2000]
]

while True:

    print("\n1.View Product")
    print("2.Add Product")
    print("3.Update Product")
    print("4.Delete Product")
    print("5.Buy")
    print("6.Search Product")
    print("7.Exit")

    ch = int(input("Enter Choice : "))

    # View
    if ch == 1:
        for p in products:
            print(p)

    # Add
    elif ch == 2:
        n = int(input("How many products to add? "))

        for i in range(n):
            pid = int(input("Enter Id : "))
            pname = input("Enter Product Name : ")
            price = int(input("Enter Price : "))

            products.append([pid, pname, price])

    # Update
    elif ch == 3:
        pid = int(input("Enter Product Id : "))
        found = False

        for p in products:
            if p[0] == pid:
                p[1] = input("New Product Name : ")
                p[2] = int(input("New Price : "))
                found = True
                print("Product Updated")
                break

        if found == False:
            print("Id Not Found")

    # Delete
    elif ch == 4:
        pid = int(input("Enter Product Id : "))
        found = False

        for p in products:
            if p[0] == pid:
                products.remove(p)
                found = True
                print("Product Deleted")
                break

        if found == False:
            print("Id Not Found")

    # Buy / Bill
    elif ch == 5:
        total = 0

        for p in products:
            total += p[2]

        print("Total Bill =", total)

    # Search
    elif ch == 6:
        pid = int(input("Enter Product Id : "))

        found = False

        for p in products:
            if p[0] == pid:
                print("Found :", p)
                found = True
                break

        if found == False:
            print("Product Not Found")

    # Exit
    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
