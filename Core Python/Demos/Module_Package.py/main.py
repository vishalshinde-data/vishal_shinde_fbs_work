#1.Direct import
#import Mypackage.module1
#import Mypackage.module2
#Mypackage.module1.greet("Vishal", "Well Come")
#Mypackage.module2.add(12, 2)

#2.From packageName.moduleName import member
#from Mypackage.module1 import greet
#greet("Sachin", "Good Morning")


#3.From packageName.moduleName import members
#from Mypackage.module2 import add,data
#add(12, 3)
#print(data)

#4.From packageName.moduleName import all
#from Mypackage.module2 import*
#add(12, 3)
#print(data)

#1.Alice
import Mypackage.module1 as m1
import Mypackage.module2 as m2
m2.add(9, 1)
print(m2.data)