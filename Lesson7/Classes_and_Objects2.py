class Employee:
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount+=1

    def displayCount(self):
        print("Total Employees = %f"%Employee.empCount)

    def displayEmployee(self):
        print("Name = ",self.name + "\nSalary = ",self.salary)

employee1 = Employee("King","500000")
employee2 = Employee("Dan","700000")
employee3 = Employee("Brio","800000")
employee4 = Employee("Brio","800000")

Employee.displayEmployee(employee1)
Employee.displayEmployee(employee2)
Employee.displayEmployee(employee3)

Employee.displayCount(employee1)