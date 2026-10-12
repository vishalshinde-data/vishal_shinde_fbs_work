from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,cno,color):
        self.cno=cno
        self.color=color

    def getCno(self):
        return self.cno
    def setCno(self,newcno):
        self.cno=newcno 

    def getColor(self):
        return self.color
    def setColor(self,newcolor):
        self.color=newcolor        

    @abstractmethod
    def breake(self):
        pass
    def __str__(self):      ##you can write here display() also
        return f"Cno={self.cno}Color{self.color}"    

class Car(Vehicle):
    def breake(self):
        print("This is the break of car")

c = Car(12, "White")            
print(c)
c.breake()