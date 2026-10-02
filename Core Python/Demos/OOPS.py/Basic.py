class Employee:
    def __init__(self):
        print("I am constructor of employee", id(self))
    def display(self):
        print("I am from display of employee")

e1 = Employee()
e2 = Employee()
print(f"id e1 = {id(e1)}")
print(f"id e1 = {id(e2)}")        