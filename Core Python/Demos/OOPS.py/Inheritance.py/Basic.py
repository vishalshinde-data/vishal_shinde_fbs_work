class Student:
    
    def __init__(self,frn,name,bname):
        self.frn=frn
        self.name=name
        self.bname=bname
        Student.stcount += 1

    def display(self):
        print(f"FRN={self.frn}\tNAME={self.name}\tBNAME={self.bname}\tStudent Count={Student.stcount}")

class PlacedStudent:
    def __init__(self,frn,name,bname,cName):
        super().__init__(frn,name,bname)
        self.cName=cName
    def setCname(self.cName):
        selfcName=self.cName
    def getName()    

            self.frn=frn
            self.name=name
            self.bname=bname
            self.cname=cname
    
    def display(self):
        print(f"FRN={self.frn}\tNAME={self.name}\tBNAME={self.bname}\tStudent Count={Student.stcount}\tCNAME={self.cname}")

s1 = Student(12, "Gaurav", "April")    
s1 = Student(1, "Atharva", "July/Aug")    
s1 = Student(53, "Rutika", "July/Aug")    
s1 = PlacedStudent(37, "Shivraj", "July/Aug", "TCS")    
s1 = PlacedStudent(18, "Virat", "July/Aug", "One8")

print(Student.stcount)