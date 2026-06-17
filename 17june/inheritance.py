####   Parent class  #####
class animal:
    type = "animal type"
    def __init__(self):
        print("default animal constructor")
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def xyz(self):
        print("hello i am from parent class ")
    def abc(self):
        print("hello is animal")  
    def greet(self):
        print("I am animal")


#### Child Class  ###

from animal import animal
class dog(animal):
    def __init__(self):
        print("child con!")    

    def __init__(self,name,weight,color):
        super().__init__(name,weight)
        self.color=color

    def abc(self):
        print("i am child class:")

    def dog_details(self):
        super().greet()
        print(f"{self.name}{self.color}")

obj=dog("badak","7kg","black")
print(obj.type)
print(obj.name)
print(obj.weight)
obj.xyz()
obj.abc()
obj.dog_details()
