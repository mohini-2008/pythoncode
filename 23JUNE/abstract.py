from abc import ABC,abstractmethod
class A(ABC):
    
    def xyz(self):
        print("hello!")
        
    @abstractmethod
    def show(self):
        pass
    
class B(A):
    def show(self):
        print("hello samiksha")
        
obj=B()
obj.xyz()
obj.show()
