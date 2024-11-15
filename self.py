class Employee: # class
    lang = "C++"
    salary = 150000

    def Get_Info(self) :
        print("Hello, I am an Employee")
        print( self.lang , self.salary)
    
    @staticmethod
    def greet():
        print("Hello, I am a function")


sunil = Employee() # object definition of class Employee
sunil.name = "Suneel"
# print(sunil.name)
# print(sunil.lang , sunil.salary)
sunil.Get_Info() # calling method Get_Info() of class Employee
# Employee.Get_Info(sunil) # calling method Get_Info() of class Employee
sunil.greet() # calling method greet() of class Employee