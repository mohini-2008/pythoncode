
### BANK ACCOUNT ###
class bank:
    def __init__(self,bankname,ifsc_code):
        self.bankname=bankname
        self.ifsc_code=ifsc_code
        
    def display_bank(self):
        return f"{self.bankname}\n{self.ifsc_code}"   




#####  ACCOUNT CLASS  ####
from bank import bank
class account(bank):
    def __init__(self,bankname,ifsc_code,aholder_name,anumber):
        super().__init__(bankname,ifsc_code)
        self.aholder_name=aholder_name
        self.anumber=anumber

    def display_bank(self):
        super().display_bank()
        return f"{self.aholder_name}\n{self.anumber}"




#### SAVING ACCOUNT ####
from account import account
class savingacc(account):
    def  __init__(self,bankname,ifsc_code,aholder_name,anumber,bal):
        super().__init__(bankname,ifsc_code,aholder_name,anumber)
        self.bal=bal

    def display_account(self):
        super().display_bank()
        return f"{self.bal}"
obj= savingacc("state bank",20289,"samiksha gaikwad",20292383746,25000)
print(obj.bankname)
print(obj.ifsc_code)
print(obj.aholder_name)
print(obj.anumber)
print(obj.bal)
