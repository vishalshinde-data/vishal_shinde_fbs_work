class Vehicle:
    def __init__(self, brand, speed, price):
        self.brand = brand
        self.speed = speed
        self.price = price

        def getBrand(self):
            return self.brand
        def setrand(self,newbrand):
            self.brand=newbrand 
        
        def getSpeed(self):
            return self.speed
        def setSpeed(self,newspeed):
            self.speed=newspeed
        
        def getPrice(self):
            return self.price
        def setPrice(self,newprice):
            self.price=newprice
        

    def display(self):
        print(f"Brand={self.brand}\tSpeed={self.speed}\tPrice={self.price}")


class Car(Vehicle):
    def __init__(self, brand, speed, price,fuelType):
        super().__init__(brand, speed, price)
        self.fuelType = fuelType

    def display(self):
        super().display()
        print(f"FuelType={self.fuelType}")


class SportsCar(Vehicle):
    def __init__(self, brand, speed, price,topSpeed):
        super().__init__(brand, speed, price)
        self.topSpeed = topSpeed

    def display(self):
        super().display()
        print(f"TopSpeed={self.topSpeed}")


v1 = Vehicle("nexon", "CNG", 1500000 )
c1 = Car("scropio", 150, 5000000, "Diesel")
sc1 = SportsCar("Porsche", 200, 200000000, 300)

v1.display()
c1.display()
sc1.display()

