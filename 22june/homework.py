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
        
choice = int(input("""
Choose Inheritance Type:
1. Single
2. Multiple
3. Multilevel
4. Hierarchical
5. Hybrid

Enter your choice: """))

match choice:

    case 1:     # Single Inheritance
        class Student:
            def details(self):
                print("Name: Rahul")

        class Result(Student):
            def marks(self):
                print("Marks: 85")

        obj = Result()
        obj.details()
        obj.marks()

    case 2:     # Multiple Inheritance
        class Sports:
            def sport_score(self):
                print("Sports Score: 20")

        class Academics:
            def academic_score(self):
                print("Academic Score: 80")

        class Student(Sports, Academics):
            pass

        obj = Student()
        obj.sport_score()
        obj.academic_score()

    case 3:     # Multilevel Inheritance
        class Person:
            def person_info(self):
                print("Person Details")

        class Student(Person):
            def student_info(self):
                print("Student Details")

        class Topper(Student):
            def topper_info(self):
                print("Topper of the Year")

        obj = Topper()
        obj.person_info()
        obj.student_info()
        obj.topper_info()

    case 4:     # Hierarchical Inheritance
        class Employee:
            def company(self):
                print("Company: ABC Pvt Ltd")

        class Manager(Employee):
            pass

        class Developer(Employee):
            pass

        m = Manager()
        d = Developer()

        m.company()
        d.company()

    case 5:     # Hybrid Inheritance
        class Vehicle:
            def fuel(self):
                print("Uses Fuel")

        class Car(Vehicle):
            pass

        class Bike(Vehicle):
            pass

        class ElectricCar(Car, Bike):
            pass

        obj = ElectricCar()
        obj.fuel()

    case _:
        print("Invalid Choice")
