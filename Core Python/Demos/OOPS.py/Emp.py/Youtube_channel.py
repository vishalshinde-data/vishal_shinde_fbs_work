class Channel:
    def __init__(self,name,subscribers,views):
        self.name=name
        self.subscribers=subscribers
        self.views=views

    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname    

    def getSubscribers(self):
        return self.subscribers
    def setSubscribers(self,newsubscribers):
        self.subscribers=newsubscribers        

    def getViews(self):
        return self.views
    def setViews(self,newviews):
        self.views=newviews   

    def display(self):
        print(f"Name={self.name}\tSubscribers={self.subscribers}\tViews={self.views}") 

c1 = Channel("Apna college", 2000000, 435673256)
c2 = Channel("Code With Hurry", 3000000, 12564836)
c3 = Channel("SoniLiv", 4000000, 934762346)   

c1.display()
c1.display()
c1.display()