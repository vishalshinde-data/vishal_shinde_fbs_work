#1.Direct import
import demo1
demo1.add(12, 4)
print(demo1.a)
print(demo1.sub(12, 3))


#2.From module Name import member
from demo1 import member
from demo1 import add
from demo1 import a
sub(12, 9)
add(12, 3)
print(a)

#3.From module Name import member
from demo1 import add,sub,a
print(a)
add(12, 7)

#4.From modulename import all
from demo1 import *
sub(12, 7)


#5.Alice name
import demo1 as d
print(d.a)
