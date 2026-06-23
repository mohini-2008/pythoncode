class account:
    def __init__(self,bal):
        self.__bal=bal
    def get_bal(self):
        return self.__bal
    def set_bal(self,amt):
        self.__bal=amt
        print("bal updated")
    
    def __private_method(self):
        return "hello i am private!"
        
    def access_pm(self):
        return self.__private_method()


        
obj=account(0)
print(obj.get_bal())
print(obj.set_bal(5000))
print(obj.get_bal())
print(obj.access_pm())
