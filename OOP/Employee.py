class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
    
    def getSalary(self):
        return self.salary
    
Aditya = Employee("Aditya Saxena",500000000)
print(Aditya.name)
print(Aditya.salary)
Aditya.getSalary()

Adi = Employee("Adi Saxena",2300000000)
print(Adi.name)
print(Adi.salary)