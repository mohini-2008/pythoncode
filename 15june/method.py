class student():
    c_name="abc"
     #class method
    @classmethod
    def change_c_name(cls):
        return "class method"
         
        
    @classmethod
    def change_c_name1(cls,new_value):
        cls.c_name=new_value
        return f"updated value is {cls.c_name}"


print(student.change_c_name())
print(student.change_c_name1("linkcode"))
