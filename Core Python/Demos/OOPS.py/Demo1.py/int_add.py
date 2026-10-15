a =10
b = 20
print(a+b)

a = "virat"
b = "kohli"
print(a+b)

a = 3.14
b = 9.1
print(a+b)

a = [1, 2, 3, 4]
b = [5, 6, 7 ,8]
print(a+b)

#a = time(1, 2, 4)
#b = time(3, 2, 4)
#print(a+b)

class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec

    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
    def __add__(self,other):
        thr=self.hr+other.hr    
        tmin=self.min+other.min   
        tsec=self.sec+other.sec   
        return Time(thr,tmin,tsec)
t1 = Time(12,33,55)
t2 = Time(6,30,56)
print(t1+t2)  


class Time:
    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
    def __add__(self,other):
        tsec=self.sec + other.sec
        emin=tsec//60
        tsec=tsec%60
        tmin=self.min + other.min+emin
        ehr=tmin//60
        tmin=tmin%60
        thr=self.hr + other.hr+ehr
        return Time(thr,tmin,tsec)

t1 = Time(12,33,55)
t2 = Time(6,30,56)
a = t1 + t2
    

    
class Time:
    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
    def __add__(self,other):
        tsec=self.sec + other.sec
        emin=tsec//60
        tsec=tsec%60
        tmin=self.min + other.min+emin
        ehr=tmin//60
        tmin=tmin%60
        thr=self.hr + other.hr+ehr
        return Time(thr,tmin,tsec)
    def __add__(self,other):
        tsec=self.sec + other.sec
        emin=tsec//60
        tsec=tsec%60
        tmin=self.min + other.min+emin
        ehr=tmin//60
        tmin=tmin%60
        thr=self.hr + other.hr+ehr
        return Time(thr,tmin,tsec)

t1 = Time(12,33,55)
t2 = Time(6,30,56)
t3 = Time(1,1,1)
a = t1 + t2 + t3
print(a)
    

    
