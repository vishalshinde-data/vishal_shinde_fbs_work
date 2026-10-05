class Student:
    def __init__(self,rollno,name,marks):
        self.rollno=rollno
        self.name=name
        self.marks=marks

    def getRollno(self):
        return self.rollno
    def setRollno(self, newrollno):
        self.rollno=newrollno  

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name=newname  

    def getMarks(self):
        return self.marks
    def setRollno(self, newmarks):
        self.marks=newmarks     

    def display(self):
        print(f"Rollno={self.rollno}\tName={self.name}\tMarks{self.marks}") 

s1 = Student(1, "ram", 98)
s2 = Student(2, "Krishna", 99)                  

s1.display()
s2.display()