class payment:
    def pay(self):
        print("Payment Process Started")

class upi(payment):
    def pay(self):
        super().pay()
        return "payment done by upi"
    
class gpay(payment):
    def pay(self):
        super().pay()
        return "payment done by gpay"
    
u=upi()
g=gpay()

print("Payment")
print("1.upi\n2.gpay\n3.card\n4.exit")
ch=int(input("enter your choice:"))
match ch:
    case 1:
        print(u.pay())
    case 2:
        print(g.pay())
    case 3:
        pass
    case 4:
        print("exit")
    case _:
        print("invalid choice")
