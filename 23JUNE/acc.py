class acc:
    def __init__(self,bal):
        self.__bal=bal
    def __dep(self):
        amount=int(input("enter amount to deposite:"))
        self.__bal+=amount
        return f"bal={self.__bal}"
    def get_dep(self):
        return self.__dep()
    def __withdraw(self):
        a=int(input("enter amount to withdraw:"))
        if a<self.__bal:
            self.__bal-=a
            return f"withdraw amount={a} \nBalance{self.__bal}"
        else:
            print("insuff... fund:")
        
    def get_withdraw(self):
        return self.__withdraw()
        
obj=acc(500)
print(obj.get_dep())
print(obj.get_withdraw())
        
        
        
        
