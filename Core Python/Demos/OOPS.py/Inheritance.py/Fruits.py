class Fruit:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def getName(self):
        return self.name
    def getName(self,newname):
        self.name=newname

    def getColor(self):
        return self.color
    def getcolor(self,newcolor):
        self.color=newcolor

    def getPrice(self):
        return self.price
    def getPrice(self,newprice):
        self.price=newprice

    def display(self):
        print(f"Name={self.name}\tColor={self.color}\tPrice{self.price}")

class CitrusFruit(Fruit):
    def __init__(self,name,color,price,taste):
        super().__init__(name,color,price)
        self.taste=taste

    def getTaste(self):
        return self.taste
    def getTaste(self,newtaste):
        self.taste=newtaste

    def display(self):
        super().display()
        print(f"Taste={self.taste}")     

class (Fruit):
    def __init__(self,name,color,price,variety):
        super().__init__(name,color,price)
        self.variety=variety
    
    def getVariety(self):
        return self.variety
    def getVariety(self,newvariety):
        self.variety=newvariety
    
    def display(self):
        super().display()
        print(f"Variety={self.variety}") 

f1 = Fruit("Apple", "Red", 120)
cf1 = CitrusFruit("Lemon", "yellow", 80, "Sour")
o1 = Orange("Orange", "Orange", 100, "Nagpur")

f1.display()
cf1.display()
o1.display()                                    