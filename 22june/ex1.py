### class product ###
class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def show(self):
        return f"{self.name}\n{self.price}"


#### class payment ###

class payment:
    def pay(self,amount):
        return f"payment of {amount} is successfull!"



#### class order #####
from product import product
from payment import payment

class order(product,payment):
    def bill(self):
        qty=int(input("enter qty"))
        total=self.price*qty
        print(self.show())
        print(self.pay(total))

obj=order("car",5000)
obj.bill()
