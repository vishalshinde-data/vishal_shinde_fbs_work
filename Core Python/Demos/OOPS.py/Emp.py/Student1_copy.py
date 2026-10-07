class Student:
    inName="fbs"
    @staticmethod
    def setInName(niname):
        Student.inName=niname
        
    def __init__(self,frn,name,bname):
        self.frn=frn
        self.name=name
        self.bname=bname

    def getFrn(self):
        return self.frn
    def serFrn(self,newfrn):
        self.frn=newfrn  

    def getName(self):
        return self.name
    def serName(self,newname):
        self.name=newname 

    def getBname(self):
        return self.bname
    def serBname(self,newbname):
        self.bname=newbname  

    
    def display(self):
        print(f"Frn={self.frn}\tName={self.name}\tBname={self.bname}\tInsname={Student.insname}")

s1 = Student(37, "Virat", "Data science", "fbs")  
s2 = Student(38, "Anushka", "Data analytics", "fbs")
s3 = Student(2, "Akay", "Python full stack", "fbs")

