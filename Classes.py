class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.Salary = salary
    def getSalary(self):
        return self.Salary





sani = Employee("MA-Sani", "9923")
print(sani.name)
print(sani.Salary)
Ali = Employee("Sani", "9998")
print(Ali.name)
print(Ali.Salary)

sani.getSalary()
Ali.getSalary()
