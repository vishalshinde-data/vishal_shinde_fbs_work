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

