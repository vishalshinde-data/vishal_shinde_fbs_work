import pickle
class Student:
    def __init__(self,rno,name,marks):
        self.rollno=rno
        self.name=name
        self.marks=marks
    def selfname(self,newname):
        self.name=newname  
    def getname(self):
        return self.name
    def __str__(self):
        return f"{self.rollno}{self.name}{self.marks}"
s1=Student(12,"vishal",67) 

with open("abc.dat",'wb+')as f:
    pickle.dump(s1,f)
    f.seek(0)
    d=pickle.load(f)
    print(d)
    print(type(d))
    d.setname("Vishal")






  
    