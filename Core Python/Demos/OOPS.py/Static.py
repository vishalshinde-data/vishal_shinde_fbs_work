class Student:
    insname="fbs"
    @staticmethod
    def setInsName(newname):
        Student.insname=newname
        
    def __init__(self,frn,name,bname):
        self.frn=frn
        self.name=name
        self.bname=bname
    
    def display(self):
        print(f"Frn={self.frn}\tName={self.name}\tBname={self.bname}\tInsname={Student.insname}")

print(Student.insname)
Student.setInsName("Firstbit Solutions")
print(Student.insname)