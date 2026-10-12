class Flight:
    def __init__(self,flightno,destination,price):
        self.flightno=flightno
        self.destination=destination
        self.price=price

    def getFlightno(self):
        return self.flightno
    def setFlightno(self,newflightno):
        self.flightno=newflightno 

    def getDestination(self):
        return self.destination
    def setDestination(self,newdestination):
        self.destination=newdestination

    def getPrice(self):
        return self.price
    def setPrice(self,newprice):
        self.price=newprice

    def calflight(self):
        print(f"Final price of ticket={self.price}")    

    def display(self):
        print(f"Flightno={self.flightno}\tDestination={self.destination}\tPrice={self.price}")
#Flight class ends here....        

class DomesticFlight(Flight):
    def __init__(self,flightno,destination,price,tax):
        super().__init__(flightno,destination,price)
        self.tax=tax

    def getTax(self):
        return self.tax
    def setTax(self,newtax):
        self.tax=newtax

    def calFlight(self):
        print(f"Final price of flight ticket={self.price+self.tax}")    

    def display(self):
        super().display() 
        print(f"Tax={self.tax}\t")       
#Domesticfkight class ensd here...

class InternationalFlight(Flight):
    def __init__(self,flightno,destination,price,charges):
        super().__init__(flightno,destination,price)
        self.charges=charges

    def getCharges(self):
        return self.charges
    def setCharges(self,newcharges):
        self.charges=newcharges

    def calFlight(self):
        print(f"Final price of flight ticket={self.price+self.charges}")        

    def display(self):
        super().display()
        print(f"Charges={self.charges}")

f1 = Flight(12, "Mumbai", 5000) 
df1 = DomesticFlight(123, "Bangalore", 10000, 5000)
if1 = InternationalFlight(223, "UAE", 30000, 2000) 

if1.calFlight()
df1.calflight()