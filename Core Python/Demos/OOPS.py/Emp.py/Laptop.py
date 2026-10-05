class Laptop:
    def __init__(self,brand,price,processor):
        self.brand=brand
        self.price=price
        self.processor=processor

    def getBrand(self):
        return self.brand
    def setBrand(self, newbrand):
        self.brand=newbrand    

    def getPrice(self):
        return self.price
    def setPrice(self, newprice):
        self.price=newprice 

    def getProcessor(self):
        return self.processor
    def setProcessor(self, newprocessor):
        self.processor=newprocessor  

    def display(self):
        print(f"Brand={self.brand}\tPrice={self.price}\tProcessor={self.processor}")

l1 = Laptop("Asus", 60000, "i10")        
l2 = Laptop("Mac", 92000, "i11")        
l3 = Laptop("Dell", 45000, "i5")

l1.display()
l2.display()
l3.display()

