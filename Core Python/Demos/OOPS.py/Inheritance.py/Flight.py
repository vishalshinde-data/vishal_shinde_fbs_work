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

    def display(self):
        print(f"Flightno={self.flightno}\tDestination={self.destination}\tPrice={self.price}")
#Flight class ends here....        

class DomesticFlight(Flight):
    def __init__(self,flightno,destination,price,state):
        super().__init__(flightno,destination,price)
        self.state=state

    def getState(self):
        return self.state
    def setState(self,newstate):
        self.state=newstate

    def display(self):
        super().display() 
        print(f"State={self.state}")       
#Domesticfkight class ensd here...

class InternationalFlight(Flight):
    def __init__(self,flightno,destination,price,country):
        super().__init__(flightno,destination,price)
        self.country=country

    def getCountry(self):
        return self.country
    def setCountry(self,newcountry):
        self.country=newcountry

    def display(self):
        super().display()
        print(f"Country={self.country}")

f1 = Flight(12, "Mumbai", 5000) 
Df1 = DomesticFlight(123, "Banglour", 10000, "Karnatak")
If1 = InternationalFlight(223, "UAE", 30000, "Dubai") 

f1.display()
Df1.display()
If1.display()



                                 