import random 
class insta:
    def __init__(self,name,username,pwd):
        self.name=name
        self.username=username
        self.__pwd=pwd
    def verify_otp(self,ur_otp):
        if self.__otp==ur_otp:
            print("Navigating to home page:")
        else:
            print("invalid otp:")
            
    def login(self,username,pwd):
        if self.username==username and self.__pwd==pwd:
            print("login succesfull....")
            self.__otp=random.randint(1000,9999)
            print("otp send to your register mobile number",self.__otp)
            ur_otp=int(input("enter otp:"))
            self.verify_otp(ur_otp)
        else:
            print("invalid creditials...")
   
        
obj=insta("ram","ram@123",12345)
obj.login("ram@123",12345)
