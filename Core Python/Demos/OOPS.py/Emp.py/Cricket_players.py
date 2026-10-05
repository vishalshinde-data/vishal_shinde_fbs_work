class Players:
    def __init__(self, no,name,runs):
        self.no=no
        self.name=name
        self.runs=runs

    def getNo(self):
        return self.no
    def setNo(self, newno):
        self.no=newno

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name=newname

    def getRuns(self):
        return self.runs
    def setNo(self, newruns):
        self.runs=newruns 

    def display(self):
        print(f"No={self.no}\tName={self.name}\tRuns={self.runs}")

p1 = Players(18, "virat", 25000)
p2 = Players(45, "rohit", 20000)
p3 = Players(7, "Dhoni", 15000)    


p1.display()
p2.display()
p3.display()