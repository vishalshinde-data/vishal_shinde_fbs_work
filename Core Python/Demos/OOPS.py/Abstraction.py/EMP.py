#You have to stored employee object using any data structure.

class Employee:

    def __init__(self, eid, name, salary):
        self.eid = eid
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.eid)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("--------------")

# Create a list
employees = []

# Create employee objects
e1 = Employee(101, "Rahul", 25000)
e2 = Employee(102, "Amit", 30000)
e3 = Employee(103, "Sneha", 35000)

# Store objects in the list
employees.append(e1)
employees.append(e2)
employees.append(e3)

# Display all employees
for emp in employees:
    emp.display()