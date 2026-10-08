class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getSalary(self):
        return self.salary
    def setSalary(self, newsalary):
        self.salary = newsalary

    def getDepartment(self):
        return self.department
    def setDepartment(self, newdepartment):
        self.department = newdepartment

    def display(self):
        print(f"Name={self.name}\tSalary={self.salary}\tDepartment={self.department}")

class Developer(Employee):
    def __init__(self, name, salary, department, language):
        super().__init__(name, salary, department)
        self.language = language

    def getLanguage(self):
        return self.language
    def setLanguage(self, newlanguage):
        self.language = newlanguage
    
    def display(self):
        super().display()
        print(f"Language={self.language}")


class SeniorDeveloper(Employee):
    def __init__(self, name, salary, department, experience):
        super().__init__(name, salary, department)
        self.experience = experience

    def getExperience(self):
        return self.experience
    def setExperience(self, newexperience):
        self.experience = newexperience   

    def display(self):
        super().display()
        print(f"Experience={self.experience}")


e1 = Employee("Rahul", 30000, "HR")
d1 = Developer("Amit", 60000, "IT", "Python")
sd1 = SeniorDeveloper("Vishal", 100000, "IT", 5)

e1.display()
d1.display()
sd1.display()