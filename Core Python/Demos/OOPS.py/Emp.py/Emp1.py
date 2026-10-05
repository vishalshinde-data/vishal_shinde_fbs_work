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
    def setSal(self, newid): # you can also give different name there.
        self.sal = newid           

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tSal={self.sal}")

e1=Employee(10,"vishal",121212)
e2=Employee(18,"virat",123431)            
e1.display()
e2.display()
#if you want to change salary
e2.setSal(147852)
e2.display()

