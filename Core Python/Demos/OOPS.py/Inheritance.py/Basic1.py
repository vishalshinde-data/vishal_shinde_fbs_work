class Employee
#Emp Ends Here.....

class Hr(Employee):
    def__init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com=com
    def getcom(self):
        return self.com
    def setCom(self,ncom):
        self.com=ncom

    def display(self):
        print(f"Com={self.com}\t")
        super().display()
#Class Hr ends Here...  

class Developer(Employee):
    def getcom(self):
        return self.com
    def setCom(self,ncom):
        self.com=ncom
    
    def display(self):
        print(f"Com={self.bonus}\t")
        return super().display() 
#Class Developer ends Here...

e1 = Employee(1, "Rahul", 3333)
h1 = Hr(7, "Harman", 8766, 9876)
d1 = Developer(63, "Surya", 6798, 3457)

e1.display()
h1.display()
d1.display()
        

    

