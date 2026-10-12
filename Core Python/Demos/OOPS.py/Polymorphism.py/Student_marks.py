class Employee:
    def __init__(self, id1, name1, sal1):
        self.id = id1
        self.name = name1
        self.sal = sal1

    def getId(self):
        return self.id
    def setId(self, newid):
        self.id = newid    

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname       

    def getSal(self):
        return self.sal
    def setSal(self, newid): 
        self.sal = newid   

    def calsal(self):
            print(f"Final salary of Emloyee={self.sal}")
    
    def display(self):
        print(f"Id={self.id}\tName={self.name}\tSal={self.sal}")

class Hr(Employee):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com=com
    def getcom(self):
        return self.com
    def setCom(self,newcom):
        self.com=newcom

    def calsal(self):
        print(f"Final salary of hr={self.sal+self.com}")

    def display(self):
        print(f"Com={self.com}\t")
        super().display()
#Class Hr ends Here...  

class Developer(Employee):
    def __init__(self,id,name,sal,bonus):
        super().__init__(id,name,sal)
        self.bonus=bonus
    def getBonus(self):
        return self.bonus
    def setBonus(self,newbonus):
        self.bonus=newbonus

    def calsal(self):
            print(f"Final salary of developer={self.sal+self.bonus}")
    
    def display(self):
        print(f"Bonus={self.bonus}\t")
        return super().display() 
#Class Developer ends Here...

e1 = Employee(1, "Rahul", 3333)
h1 = Hr(7, "Harman", 8766, 9876)
d1 = Developer(63, "Surya", 6798, 3457)

d1.calsal()
e1.calsal()
h1.calsal()
        

    


