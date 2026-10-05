class Flight:
    def __init__(self,flightno,distination,price):
        self.flightno=flightno
        self.distination=distination
        self.price=price

    def getFlightno(self):
        return self.flightno
    def setFlightno(self,newflightno):
        self.flightno=newflightno     

    def getDistination(self):
        return self.distination
    def setDistination(self,newdistination):
        self.distination=newdistination         

    def getPrice(self):
        return self.price
    def setPrice(self,newprice):
        self.price=newprice   

    def display(self):
        print(f"Flightno={self.flightno}\tDistination={self.distination}\tPrice={self.price}")

f1 = Flight(101, "Pune", 5000)      
f2 = Flight(102, "Mumbai", 10000) 
f3 = Flight(103, "Delhi", 15000)   

f1.display()
f2.display()
f3.display()