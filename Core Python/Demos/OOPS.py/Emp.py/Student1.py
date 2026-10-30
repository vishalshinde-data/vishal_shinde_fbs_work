class Student:
    def __init__(self,frn,name,bname,insname):
        self.frn=frn
        self.name=name
        self.bname=bname
        self.insname=insname

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

    def getInsname(self):
        return self.insname
    def serInsname(self,newinsname):
        self.insname=newinsname   

    def display(self):
        print(f"Frn={self.frn}\tName={self.name}\tBname={self.bname}\tInsname={self.insname}")

s1 = Student(37, "Virat", "Data science", "fbs")  
s2 = Student(38, "Anushka", "Data analytics", "fbs")
s3 = Student(2, "Akay", "Python full stack", "fbs")

s1.display()
s2.display()
s3.display()








class Student:
    def __init__(self,frn,name,bname,insname):
        self.frn=frn
        self.name=name
        self.bname=bname
        self.insname=insname

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

    def getInsname(self):
        return self.insname
    def serInsname(self,newinsname):
        self.insname=newinsname   

    def display(self):
        print(f"Frn={self.frn}\tName={self.name}\tBname={self.bname}\tInsname={self.insname}")

s1 = Student(37, "Virat", "Data science", "fbs")  
s2 = Student(38, "Anushka", "Data analytics", "fbs")
s3 = Student(2, "Akay", "Python full stack", "fbs")

s1.display()
s2.display()
s3.display()